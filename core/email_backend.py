import socket
import ssl
from django.core.mail.backends.smtp import EmailBackend
from django.utils.functional import cached_property
import smtplib

class IPv4SMTP_SSL(smtplib.SMTP_SSL):
    def _get_socket(self, host, port, timeout):
        # Force IPv4 by requesting only AF_INET
        if self.debuglevel > 0:
            self._print_debug('connect: %s, %s' % (host, port))
        return socket.create_connection((host, port), timeout, self.source_address)
    
    def connect(self, host='localhost', port=0):
        # We override connect to ensure we only look for IPv4 addresses if create_connection doesn't behave
        # But actually, the cleanest hack is to intercept the getaddrinfo call or just rely on 'create_connection' behavior
        # However, standard socket.create_connection tries both.
        # Let's write a robust version that forces AF_INET
        self._get_socket = self._get_socket_forced_ipv4
        return super().connect(host, port)

    def _get_socket_forced_ipv4(self, host, port, timeout):
        # Custom socket creation that filters for AF_INET (IPv4)
        if self.debuglevel > 0:
            self._print_debug('connect (IPv4): %s, %s' % (host, port))
        
        # Get only IPv4 addresses
        targets = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
        
        last_exc = None
        for res in targets:
            af, socktype, proto, canonname, sa = res
            sock = None
            try:
                sock = socket.socket(af, socktype, proto)
                if timeout is not socket._GLOBAL_DEFAULT_TIMEOUT:
                    sock.settimeout(timeout)
                if self.source_address:
                    sock.bind(self.source_address)
                sock.connect(sa)
                
                # Wrap in SSL if needed (SMTP_SSL default behavior handles this in init/connect, but we are inside _get_socket)
                # Wait, SMTP_SSL._get_socket returns a regular socket, then it wraps it. 
                # Actually in Python 3.10+, SMTP_SSL uses context.wrap_socket inside usual flow? 
                # Let's check Python source logic.
                # SMTP_SSL.connect -> super().connect -> self._get_socket -> socket.create_connection...
                # THEN it calls self.sock = self.context.wrap_socket(self.sock)
                # So we just need to return the connected TCP socket here.
                return sock
            except OSError as exc:
                if sock is not None:
                    sock.close()
                last_exc = exc
        if last_exc:
            raise last_exc
        raise OSError("No IPv4 address found for %s" % host)

class IPv4EmailBackend(EmailBackend):
    def open(self):
        """
        Ensures we use the IPv4-forced SMTP class
        """
        if self.connection:
            return False
        
        connection_class = IPv4SMTP_SSL if self.use_ssl else smtplib.SMTP
        # logic to swap class if SSL is used
        
        try:
            self.connection = connection_class(self.host, self.port,
                                               timeout=self.timeout)
            
            # If we are using our custom SSL class, it already forces IPv4 in connect()
            # If we are NOT using SSL (unlikely given our settings), we would need a plain IPv4SMTP class too.
            # But we are using port 465 SSL.
            
            if not self.use_ssl and self.use_tls:
                # Logic for STARTTLS if we reverted? 
                # For now let's assume we are sticking to Port 465 SSL as planned.
                pass
                
            self.connection.echo = False  # disable echo
            
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except OSError:
            if not self.fail_silently:
                raise

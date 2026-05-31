from django.conf import settings

def google_analytics(request):
    """
    Exposes the Google Analytics ID globally to all templates.
    """
    return {
        'GOOGLE_ANALYTICS_ID': getattr(settings, 'GOOGLE_ANALYTICS_ID', '')
    }

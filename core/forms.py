from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full px-3 py-2 border border-app-border rounded-md shadow-sm placeholder-app-text-muted focus:outline-none focus:ring-app-accent focus:border-app-accent sm:text-sm bg-app-surface text-app-text-main',
            'placeholder': 'Your Name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'appearance-none block w-full px-3 py-2 border border-app-border rounded-md shadow-sm placeholder-app-text-muted focus:outline-none focus:ring-app-accent focus:border-app-accent sm:text-sm bg-app-surface text-app-text-main',
            'placeholder': 'you@example.com'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'appearance-none block w-full px-3 py-2 border border-app-border rounded-md shadow-sm placeholder-app-text-muted focus:outline-none focus:ring-app-accent focus:border-app-accent sm:text-sm bg-app-surface text-app-text-main h-32',
            'placeholder': 'How can I help you?'
        })
    )

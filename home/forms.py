from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='Your Email')
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)

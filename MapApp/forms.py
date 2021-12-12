from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Antonio Garzia Martinez'}), required=True)

    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'myname@email.com'}), required=True)

    subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}), required=True)

    message = forms.CharField(label='Message', max_length=500, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3, 'cols': 40, }), required=True)

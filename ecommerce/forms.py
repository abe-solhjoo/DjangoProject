from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if 'gmail.com' not in email:
            raise forms.ValidationError('You should enter gmail.com only')

        return email


class LoginForm(forms.Form):
    userName = forms.CharField(
        widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Enter your user name'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput({'class': 'form-control', 'placeholder': 'Enter your password'})
    )
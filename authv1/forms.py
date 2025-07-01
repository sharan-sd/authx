from django import forms
from .models import UserAccounts

# Signup Form
class RegisterForm(forms.ModelForm):
    email = forms.EmailField(max_length=75, required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, required=True)
    password_confirm = forms.CharField(max_length=100, widget=forms.PasswordInput, required=True)


    class Meta:
        model = UserAccounts
        fields = ['email', 'password']

    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm:
            if password == password_confirm:
                if len(password) >= 8:
                    if (
                        any(c.isupper() for c in password) and 
                        any(c.isdigit() for c in password) and 
                        any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/`~" for c in password)
                    ):
                        pass
                    else:
                        raise forms.ValidationError(message="Password must contain at least 1 uppercase letter, 1 number, and 1 special character")
                else:
                    raise forms.ValidationError(message="Password must have 8 character")
            else:
                raise forms.ValidationError(message="Password do not match")
    
        return cleaned_data
    

# SignIn Form
class SignInForm(forms.Form):
    email = forms.EmailField(max_length=75, required=True)
    password = forms.CharField(max_length=100, required=True)
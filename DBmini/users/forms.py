from django import forms
from django.contrib.auth.models import User
from .models import Event, Registration

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150, 
        required=True, 
        help_text='',  # Removes the default help text
    )
    password = forms.CharField(widget=forms.PasswordInput, label="Password") # forms.PasswordInput as a widget to hide the password input
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    # ensures that passwoed and confirm password field matches
    def clean(self):
        cleaned_data = super().clean() # returning a dictionary of cleaned data (cleaned_data) that includes all the form's validated fields.
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

        return cleaned_data

    # This method saves the user data to the database, ensuring that the password is securely hashed.
    def save(self, commit=True):
        user = super().save(commit=False) # This creates a User object but does not save it to the database yet. Using commit=False allows us to modify the object before saving it.
        user.set_password(self.cleaned_data["password"])  # user.set_password() for hashing the password (Instead of saving the password directly, set_password is used, which hashes the password. Django’s set_password method ensures that the password is stored securely.)
        if commit:
            user.save()
        return user


# since admins/organisers are added by creating superuser commands, for adminlogin we don't need a modelform instead we use regular form
class AdminLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150, 
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'end_date', 'description', 'image', 'category']  # Include the fields you want in the form

class UserEventRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone']
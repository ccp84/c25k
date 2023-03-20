from django import forms
from .models import Profile, Run


class DateInput(forms.DateInput):
    input_type = "date"


class ProfileForm(forms.ModelForm):
    """
    Form for adding a user profile.
    Includes date picker widget
    """
    class Meta:
        model = Profile
        widgets = {
            "DOB": DateInput(),
        }
        fields = ['DOB', 'ICE', 'medical']


class ProfileUpdateForm(forms.ModelForm):
    """ Form for updating a user profile. """
    class Meta:
        model = Profile
        fields = ['DOB', 'ICE', 'medical']


class RunForm(forms.ModelForm):
    """
    Form for adding a new run.
    Includes date picker widget.
    """
    class Meta:
        model = Run
        widgets = {
            "date": DateInput(),
        }
        fields = ["title", "leader", "location", "date", "time", "details"]


# Code taken from:
# https://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
class SignupForm(forms.Form):
    """
    Form extension to standard allauth sign up form.
    Inclusion of first and last name fields on sign up.
    """
    first_name = forms.CharField(
        max_length=30, label='First Name', required=True)
    last_name = forms.CharField(
        max_length=30, label='Last Name', required=True)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

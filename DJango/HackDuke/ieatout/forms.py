from django import forms
from ieatout.models import UserProfile

class UserProfileForm(forms.ModelForm):
        
    name = forms.CharField(max_length=128, help_text="Please enter your name.")
    gender = forms.CharField(max_length=128, help_text="Please enter your sex.")
    location = forms.CharField(max_length=128, help_text="Please enter your address.")
    state = forms.CharField(max_length=128, help_text="Please enter your preference.")
    allergy = forms.CharField(max_length=128, help_text="Please enter your allergy.")
    health = forms.CharField(max_length=128, help_text="Please enter your health restriction.")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = UserProfile
        fields = ('name','gender','location','state','allergy','health',)
        



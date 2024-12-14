from django.forms import ModelForm

from LiftHub.accounts.models import Profile


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['slug', 'user', 'is_completed']

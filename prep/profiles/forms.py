from django import forms

from prep.mixins import ReadOnlyMixin
from profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(ReadOnlyMixin, ProfileForm):
    readonly_fields = ['username', 'email', 'age']
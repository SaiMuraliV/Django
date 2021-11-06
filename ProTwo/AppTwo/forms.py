from django import forms
from AppTwo.models import UserInfo

class NewUserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'
        
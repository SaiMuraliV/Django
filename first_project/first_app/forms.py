from django import forms
from django.core import validators

# customized validators 
def check_for_z(value):
    if value[0].lower() != 'm':
        raise forms.ValidationError("Name need to start with m ")

class UserForm(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter email")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']
        
        if email != verify_email:
            raise forms.ValidationError("Email is not matched")

    # customized in built validatores
    # botcatcher = forms.CharField(
    #     required=False,
    #     widget=forms.HiddenInput,
    # )
    
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data["botcatcher"]
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
    #  end of customized validatores

    # bulit in validatores
    # botcatcher = forms.CharField(
    #     required=False,
    #     widget=forms.HiddenInput,
    #     validatores=[validators.MaxLengthValidator(0)])

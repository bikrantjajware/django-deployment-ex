from django import forms
from django.forms import ModelForm
from first_app.models import Users

class login(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

class SignUp(forms.ModelForm):
    class Meta:         # use of Meta(): is same as Meta:
        model = Users
        fields = "__all__"

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="enter your email again")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("email do not match")
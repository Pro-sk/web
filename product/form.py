from .models import Users
from django import forms
from django.forms import ModelForm
class Signup(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('uname','uphone','upass','uemail','city','state','zip','uadd')

        widgets = {
            'uadd' : forms.Textarea(attrs={'rows':'5','class':'form-control'}),
            'upass': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Your Password'}),
            'uphone': forms.NumberInput(attrs={'class':'form-control','placeholder':'Your Phone Number'}),
            'uname': forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),
            'uemail': forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email'}),
            'city': forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'zip': forms.NumberInput(attrs={'class':'form-control','placeholder':'Zipcode'}),
            'state': forms.TextInput(attrs={'class':'form-control','placeholder':'State'}),
        }

class Login(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['uphone','upass']
        widgets = {
            'upass': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Your Password'}),
            'uphone': forms.NumberInput(attrs={'class':'form-control','placeholder':'Your Phone Number'})
        }
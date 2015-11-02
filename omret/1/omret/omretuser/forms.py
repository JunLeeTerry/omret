#!-*-coding:utf-8-*-
from django import forms
from django.forms import ModelForm
from omret.omretuser.models import UserProfile

#class UserProfileSetForm(forms.ModelForm):
#    class Meta:
#        model = UserProfile
#        fields = ('realname','sex','birthday','signature','resume')
    


class UserProfileSetForm(forms.Form):
    realname = forms.CharField(widget=forms.TextInput(
            attrs={"id":"profile-realname",
                   "class":"form-control"
                   }))
    sex = forms.CharField(widget=forms.RadioSelect(
            choices=(('F','男'),('M','女'))))
    birthday = forms.DateField(widget=forms.DateTimeInput())
    signature = forms.CharField(widget=forms.TextInput(
            attrs={"id":"profile-signature",
                   "class":"form-control"
                   }))
    resume = forms.CharField(widget=forms.TextInput(
            attrs={"id":"profile-resume",
                   "class":"form-control"
                   }))



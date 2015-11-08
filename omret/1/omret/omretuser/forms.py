#!-*-coding:utf-8-*-
from django import forms
from django.forms import ModelForm
from omret.omretuser.models import UserProfile

#class UserProfileSetForm(forms.ModelForm):
#    class Meta:
#        model = UserProfile
#        fields = ('realname','sex','birthday','signature','resume')
    


class UserProfileSetForm(forms.Form):
    realname = forms.CharField(required=False,
                               widget=forms.TextInput(
            attrs={"id":"profile-realname",
                   "class":"form-control"
                   }))
    sex = forms.CharField(required=False,
                          widget=forms.RadioSelect(
            choices=(('F','男'),('M','女'))))
    birthday = forms.DateField(required=False,
                               widget=forms.TextInput(
            attrs={"class":"form-control",
                   "type":"text",
                   "readonly":"readonly",
                   #"disabled":"disabled",
                  
            }))
    signature = forms.CharField(required=False,
                                widget=forms.TextInput(
            attrs={"id":"profile-signature",
                   "class":"form-control"
                   }))
    resume = forms.CharField(required=False,
                             widget=forms.Textarea(
            attrs={"id":"profile-resume",
                   "class":"form-control textarea"
                   }))



from django import forms


##---------the forms
class NewsArtiForm(forms.Form):
    title = forms.CharField(required=False,
                            widget=forms.TextInput(
                                attrs={"id":"titleform",
                                       "class":"form-control"}
                            ))


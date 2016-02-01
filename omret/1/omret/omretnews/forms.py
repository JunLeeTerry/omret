from django import forms


##---------the forms
class NewsArtiForm(forms.Form):
    title = forms.CharField(required=False,
                            widget=forms.TextInput(
                                attrs={"id":"titleform",
                                       "class":"form-control"}
                            ))
    topic = forms.CharField(required=False,
                            widget=forms.Select(
                                attrs={"id":"topicselector",
                                       "class":"select form-control"}
                            ))


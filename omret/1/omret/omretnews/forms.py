from django import forms
from omret.omretnews.models import Topic


##---------the forms of post arti--------
class NewsArtiForm(forms.Form):
    # print Topic.objects.all()

    ##-------the form of title------------
    title = forms.CharField(required=False,
                            widget=forms.TextInput(
                                attrs={"id": "titleform",
                                       "class": "form-control"}
                            ))

    ##--------get topic names from db--------
    TOPIC_CHOICE = []
    for topicobject in Topic.objects.all():
        TOPIC_CHOICE.append((topicobject.name, topicobject.name))

    ##-------test the topic choices in sql--------
    print TOPIC_CHOICE

    ##-------the form of topic---------
    topic = forms.CharField(required=False,
                            widget=forms.Select(
                                attrs={"id": "topicselector",
                                       "class": "select form-control"},
                                choices=TOPIC_CHOICE
                            ))

    content = forms.CharField(required=False,
                              widget=forms.Textarea(
                                  attrs={"id": "omrettinymce"}
                              ))


##-------new qulickly comment form (textarea)--------
class NewQulicklyCommentForm(forms.Form):
    content = forms.CharField(required=True,
                              widget=forms.Textarea(
                                  attrs={"id": "newcomment",
                                         "style": "resize:none", }
                              ))


##-------new qulickly chat form (input)-------
class NewQulicklyChatForm(forms.Form):
    content = forms.CharField(required=True,
                              widget=forms.Textarea(
                                  attrs={"id": "newchat",
                                         "style": "resize:none",
                                         "autoHeight":"true",
                                         }
                              ))

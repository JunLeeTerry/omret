from django import forms
from omret.omretnews.models import Topic

##---------the forms of post arti--------
class NewsArtiForm(forms.Form):
    #print Topic.objects.all()

    ##-------the form of title------------
    title = forms.CharField(required=False,
                            widget=forms.TextInput(
                                attrs={"id":"titleform",
                                       "class":"form-control"}
                            ))

    ##--------get topic names from db--------
    TOPIC_CHOICE = []
    for topicobject in Topic.objects.all():
        TOPIC_CHOICE.append((topicobject.name,topicobject.name))
    print TOPIC_CHOICE

    ##-------the form of topic---------
    topic = forms.CharField(required=False,
                            widget=forms.Select(
                                attrs={"id":"topicselector",
                                       "class":"select form-control"},
                                choices=TOPIC_CHOICE
                            ))


#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from omret.logreg.models import User
from omret.omretnews.models import Topic
from omret.omretuser.views import hasUserSession,getUserFromSession

# Create your views here.
def index(req):

    if not hasUserSession(req):
        return HttpResponseRedirect('/')
    
    ##-------if no session or cannot find user by session,turn to login page----
    user = getUserFromSession(req)
    
    ##-------get all topics from sql--------
    topics = Topic.objects.all()
    for i in topics:
        print str(i)

    response = render_to_response('index.html',{'username':user.name,'topiclist':topics})
    return response

#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from omret.logreg.models import User

# Create your views here.
def index(req):

    try:
        uid = req.session.get('uid')
        user = User.objects.get(uid=uid)
    
    ##-------if no session or cannot find user by session,turn to login page----
    except:
        return HttpResponseRedirect('/')

    response = render_to_response('index.html',{'username':user.name})
    return response

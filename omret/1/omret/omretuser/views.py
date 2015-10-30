#-*- coding:utf-8 -*- 
from django.shortcuts import render_to_response
from omret.logreg.models import User
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

##-------user setting page --------
def settings(req):

    try:
        ##------get user session info------
        uid = req.session.get('uid')
        user = User.objects.get(uid=uid)
    ##------if theres no session,turn to the home page-----
    ##------uf no user, turn to the home page----
    except:
        return HttpResponseRedirect('/')
    
    response = render_to_response('usersettings.html',{'username':user.name})
    return response

##--------click omret brand-------
def userhome(req):
    try:
        uid = req.session.get('uid')
        user = User.objects.get(uid=uid)
        return HttpResponseRedirect('/index/')

    except:
        return HttpResponseRedirect('/')
    

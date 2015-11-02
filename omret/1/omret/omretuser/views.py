#-*- coding:utf-8 -*- 
from django.shortcuts import render_to_response
from omret.logreg.models import User
from django.http import HttpResponse,HttpResponseRedirect
from omret.omretuser.forms import UserProfileSetForm

# Create your views here.

##-------user profile setting page --------
def profileset(req):
    ##------if theres no session,turn to the home page-----
    if not hasUserSession(req):
        return HttpResponseRedirect('/')
    
    user = getUserFromSession(req)
    profileform = UserProfileSetForm
    response = render_to_response('profileset.html',{'username':user.name,'profile_form':profileform})
    return response

##------user security setting page--------
def securityset(req):
    if not hasUserSession(req):
        return HttpResponseRedirect('/')
    
    user = getUserFromSession(req)
    response = render_toresponse('securityset.html',{'username':user.name})

##--------click omret brand-------
def userhome(req):
    if hasUserSession(req):
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/')
    

##--------judge whether has user session------
##-------if has user session,return user-----
def getUserFromSession(req):
    try:
        uid = req.session.get('uid')
        user = User.objects.get(uid=uid)
        return user
    except:
        return None

def hasUserSession(req):
    user = getUserFromSession(req)
    if user == None:
        return False
    else:
        return True

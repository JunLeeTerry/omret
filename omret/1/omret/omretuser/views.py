#-*- coding:utf-8 -*- 
from django.shortcuts import render_to_response
from omret.logreg.models import User
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

##-------user setting page --------
def settings(req):
    ##------get user session info------
    uid = req.session.get('uid')
    ##------if theres no session,turn to the home page-----
    if (uid == None):
        return HttpResponseRedirect('/')

    user = User.objects.get(uid=uid)
    ##------uf no user, turn to the home page----
    if(user == None):
        return HttpResponseRedirect('/')
    else:
        response = render_to_response('usersettings.html',{})
    
    return response

#-*- coding:utf-8 -*- 
from django.shortcuts import render_to_response,RequestContext
from omret.logreg.models import User
from omret.omretuser.models import UserProfile
from django.http import HttpResponse,HttpResponseRedirect
from omret.omretuser.forms import UserProfileSetForm

from django.views.decorators.csrf import csrf_protect,csrf_exempt
# Create your views here.

##-------user profile setting page --------
@csrf_protect
def profileset(req):
    ##------if theres no session,turn to the home page-----
    if not hasUserSession(req):
        return HttpResponseRedirect('/')
    
    user = getUserFromSession(req)
    profileform = UserProfileSetForm
    response = render_to_response('profileset.html',{'username':user.name,'profile_form':profileform},
                                  context_instance=RequestContext(req))


    ##-------handle the post info after clicking the submit button-------
    if req.method == 'POST':
        profileformPost = UserProfileSetForm(req.POST)
        print profileformPost.is_valid()
        print profileformPost.errors
        if profileformPost.is_valid():
            realname = profileformPost.cleaned_data['realname']
            sex = profileformPost.cleaned_data['sex']
            birthday = profileformPost.cleaned_data['birthday']
            signature = profileformPost.cleaned_data['signature']
            resume = profileformPost.cleaned_data['resume']
            
            ##------get userprofile-------
            ##----if have not created before,create a new object then modify the value of fields----
            ##----if there is a userprofile object modify the value of fields---
            userprofile = UserProfile.object.get(user=user)
            
            if userprofile is None:
                userprofile = UserProfile()
                userprofile.user = user
            __setUserProfile(userprofile,realname,sex,birthday,signature,resume)
            
            
   
    return response

##------user security setting page--------
@csrf_protect
def securityset(req):
    if not hasUserSession(req):
        return HttpResponseRedirect('/')
    
    user = getUserFromSession(req)
    response = render_toresponse('securityset.html',{'username':user.name})

##--------click omret brand-------
@csrf_protect
def userhome(req):
    if hasUserSession(req):
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponseRedirect('/')
    

##--------judge whether has user session------
##-------if has user session,return user-----
@csrf_protect
def getUserFromSession(req):
    try:
        uid = req.session.get('uid')
        user = User.objects.get(uid=uid)
        return user
    except:
        return None

@csrf_protect
def hasUserSession(req):
    user = getUserFromSession(req)
    if user == None:
        return False
    else:
        return True

@csrf_protect
##---------set the values of profile forms into UserProfile Object----- 
def __setUserProfile(userprofile,user,realname,sex,birthday,signature,resume):
    userprofile.realname = realname
    userprofile.sex = sex
    userprofile.birthday = birthday
    userprofile.signature = signature
    userprofile.resume = resume

#-*- coding:utf-8 -*- 
from django.shortcuts import render_to_response,RequestContext
from omret.logreg.models import User
from omret.omretuser.models import UserProfile
from django.http import HttpResponse,HttpResponseRedirect
from omret.omretuser.forms import UserProfileSetForm,UserSecuritySetForm
from omret.logreg.pwencryption import pwEncryption

from django.views.decorators.csrf import csrf_protect,csrf_exempt
# Create your views here.

##-------user profile setting page --------
@csrf_protect
def profileset(req):
    ##------if theres no session,turn to the home page-----
    if not hasUserSession(req):
        return HttpResponseRedirect('/')
    
    user = getUserFromSession(req)

    ##-----if there is a user profile,the forms show the init values-----
    try:
        userprofile = UserProfile.objects.get(user_id = user.id)
        profileform = UserProfileSetForm(initial={'realname':userprofile.realname,'sex':userprofile.sex,'birthday':userprofile.birthday,'signature':userprofile.signature,'resume':userprofile.resume})
    except Exception,e:
        #print e
        profileform = UserProfileSetForm()
    
    ##----change status shows whether user change value success----
    '''
    -success  :click post button and success
    -error    :click post button and error
    -normal   :have not click the post button
    '''
    change_status = 'normal'
    ##-------handle the post info after clicking the submit button-------
    if req.method == 'POST':
        profileformPost = UserProfileSetForm(req.POST)
        
        ##-----test the profile form post-------
        #print profileformPost.is_valid()
        #print profileformPost.errors

        if profileformPost.is_valid():
            realname = profileformPost.cleaned_data['realname']
            sex = profileformPost.cleaned_data['sex']
            birthday = profileformPost.cleaned_data['birthday']
            signature = profileformPost.cleaned_data['signature']
            resume = profileformPost.cleaned_data['resume']
            
            ##------get userprofile-------
            '''
            if have not created before,create a new object then modify the value of fields
            if there is a userprofile object modify the value of fields
            '''
            try:
                userprofile = UserProfile.objects.get(user=user)
            except:
                userprofile = UserProfile()
                
            ##------set the values of fields into table user profile-----
            __setUserProfile(userprofile,user,realname,sex,birthday,signature,resume)
            
            ##------set change_status equals success if save user profile succeddfully------
            try:
                userprofile.save()
                change_status = 'success'
            except:
                change_status = 'error'

    response = render_to_response('profileset.html',{'change_status':change_status,'username':user.name,'profile_form':profileform},context_instance=RequestContext(req))
               
    return response

##------user security setting page--------
@csrf_protect
def securityset(req):
    if not hasUserSession(req):
        return HttpResponseRedirect('/')
    
    user = getUserFromSession(req)    
    securityform = UserSecuritySetForm()

    '''
    passwd change status:
    -success :passwd change successfully
    -error1  :old passwd is wrong
    -error2  :new_passwd is different from confirm_new_passwd
    -error3  :old passwd or new passwd can not be blank
    -error4  :save error
    -normal  :have not click the post button
    '''
    change_status = 'normal'
    ##-------handle the post info after clicking the submit button----
    if req.method == 'POST':
        securityformPost = UserSecuritySetForm(req.POST)
        
        if securityformPost.is_valid():
            ##-------get infomations of the forms--------
            old_password = securityformPost.cleaned_data['old_password']
            new_password = securityformPost.cleaned_data['new_password']
            confirm_new_password = securityformPost.cleaned_data['confirm_new_password']
            ##------test form data-----
            #print new_password is u'' 

            ##-------get the value of old password and encrypted------
            old_password_encryption =  pwEncryption().encryptionByPasswd(old_password)
            ##-----old_password or new_password is blank-------
            if new_password is u'' or old_password is u'':
                change_status = 'error3'
            ##-----old_password is different from passwd in sql------
            elif old_password_encryption != user.password:
                #print old_password_encryption,user.password
                change_status = 'error1'
            ##-----new_password is different from confirm_new_password----
            elif new_password != confirm_new_password:
                change_status = 'error2'
            ##-----successful------
            else:
                user.password = pwEncryption().encryptionByPasswd(new_password)
                try:
                    user.save()
                    change_status = 'success'
                except:
                    change_status = 'error4'
            

    response = render_to_response('securityset.html',{'change_status':change_status,'username':user.name,'security_form':securityform},context_instance=RequestContext(req)) 
    return response

##--------click omret brand-------
@csrf_protect
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

##---------set the values of profile forms into UserProfile Object----- 
def __setUserProfile(userprofile,user,realname,sex,birthday,signature,resume):
    userprofile.user = user
    userprofile.realname = realname
    userprofile.sex = sex
    userprofile.birthday = birthday
    userprofile.signature = signature
    userprofile.resume = resume

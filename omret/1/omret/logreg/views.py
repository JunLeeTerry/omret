#-*- coding:utf-8 -*- 
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from omret.logreg.models import User,UserActivationCode
from django import forms

import hashlib
import re

from django.views.decorators.csrf import csrf_protect,csrf_exempt
#from ValidateCodeUtil import ValidateCodeUtil
import json
import uuid

###------the part of defining method-------
def __validateEmail(account):
    account_type = None
    if len(account) > 7:
        #print 'enter >7'
        p = re.compile(r'^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,3}|[0-9]{1,3})(\]?)$')
        if p.match(account) != None:
            ##------value:1 means account is email--------
            account_type = 1
    ##----value:0 means account is username------
        else:
            account_type = 0
    else:
        account_type = 0
    return account_type

##----- define the model of form ------
##----- this form is for user signning up -------
class UserSignupForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
            attrs={"id":"signup-name",
                   "class":"form-control",
                   "placeholder":"Username"
                   }))
    password = forms.CharField(widget=forms.PasswordInput(
            attrs={"id":"signup-password",
                   "class":"form-control",
                   "placeholder":"Password"
                   }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
            attrs={"id":"signup-confirmpassword",
                   "class":"form-control",
                   "placeholder":"Confirm Password"
                   }))
    email = forms.EmailField(widget=forms.TextInput(
            attrs={"id":"signup-email",
                   "class":"form-control",
                   "placeholder":"Email"
                   }))


##------ this form is for user logining in--------
class UserLoginForm(forms.Form):
##-----account is email or username------
    account = forms.CharField(widget=forms.TextInput(
            attrs={"id":"login-account",
                   "class":"form-control",
                   "placeholder":"Email or Username",
                   }))
    password = forms.CharField(widget=forms.PasswordInput(
            attrs={"id":"login-password",
                   "class":"form-control",
                   "placeholder":"Password",
                   }))



##----- Create your views here. ------
##################################
#            signup              #
##################################
@csrf_protect
def signup(req):
    #repeat_field = None
    if req.method == 'POST':
        signup_form = UserSignupForm(req.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data['name']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']
            confirm_password = signup_form.cleaned_data['confirm_password']
            
            if password != confirm_password:
                return render_to_response('signup.html',{'signup_form':signup_form},context_instance=RequestContext(req))


            ##-----detect whether the field is repeated-----
            ##---now! use ajax in js to detect field----

            #try:
            #    if User.objects.get(name=username)!= None:
            #        repeat_field = u'name_repeat'
            #
            #    elif User.objects.get(email=email) != None:
            #        repeat_field = u'email_repeat'
            #except:
            #    pass
            #if repeat_field != None:
            #    #print repeat_field
            #    return render_to_response('signup.html',{'signup_form':signup_form,'repeat_field':repeat_field}
            #                              ,context_instance=RequestContext(req))
        
            

            ##-------no field is repeated---------
            user = User()
            user.name = username
            ##-------format the encode of man's name------
            #if isinstance(username, unicode):
            #   username = username.encode('utf-8')
            user.email = email
            user.password = password            
            user.is_active = False
            
            ##-------if click refresh button on validateemail page------
            try:
                user.save()
            except Exception,e:
                return render_to_response('validatemail.html',{'username':user})

            ##-------gen activation code--------- 
            code = uuid.uuid1().hex
            user_activation_code = UserActivationCode()
        
            user_activation_code.user = user
            user_activation_code.activation_code = code
            user_activation_code.save()
            #print user_activation_code.activation_code
            ##------send email  username + activation_code-----
            ##-----this option should in a thread i think -----
            user_activation_code.send_activation_email()
            ##-----test------
            #print signup_form.cleaned_data

            ##-----redirect to to-check-email page------
            #return HttpResponse('validate email to finish signing up')
            return render_to_response('validatemail.html',{'username':user})
    else:
        signup_form = UserSignupForm()
    return render_to_response('signup.html',{'signup_form':signup_form},context_instance=RequestContext(req))



def validatemail(req):
    name_back = req.GET.get('username')
    code_back = req.GET.get('code')
    user_back = User.objects.get(name=name_back)

    if user_back != None:
        ##-----uac means UserActivationCode-----
        uac = UserActivationCode.objects.get(user=user_back)
        #print uac.user.name,uac.activation_code,code_back
        if uac.activation_code == code_back:
            user_back.is_active = True
            user_back.save()
            uac.activation_code = u'already_activated'
            uac.save()
            return HttpResponse('sign up ok!')
    return HttpResponse('sign up error')
        


#############################
#          login            #
#############################
@csrf_protect
def login(req):
    status = u''
    is_valid = None
    ##-------if it has cookie,request change to post and is valid---------
    if req.COOKIES.get('username')!=None:
            req.method = 'POST'
            is_valid = True

    if req.method == 'POST':
        login_form = UserLoginForm(req.POST)
        if(is_valid == None):
            is_valid = login_form.is_valid()
        if is_valid:
            ##----if no cookie,get the enter infomation------
            #print req.COOKIES.get('username')
            if (req.COOKIES.get('username') == None):
                account = login_form.cleaned_data['account']
                password = login_form.cleaned_data['password']
                encrypted_password = hashlib.sha1(password).hexdigest()
            ##----if it has cookies,get the info from cookies------
            else :
                account = req.COOKIES.get('username')
                encrypted_password = req.COOKIES.get('id')
                #print account
                #print encrypted_password
                
            account_type = __validateEmail(account)
            ##----print encrypted password-----
            #print 'encrypted_password: '+encrypted_password
            ##---ensure the type of acount - username or eamil-----
            #print account_type
            if account_type == 0:
                try:
                    user = User.objects.get(name=account,password=encrypted_password)
                    status = u'success'
                except Exception,e:
                    status = u'error'
                    
                    #print e
            elif account_type == 1:
                try:
                    User.objects.get(email=account,password=encrypted_password)
                    status = u'success'
                except:
                    status = u'error'
            ##----judge the status------
            #print status
            if status == u'success':
                ##-----get rememberme checkbox value------
                rmbme = req.POST.get("rmbme")

                ##-----gen the session and store into the cookie------
                ##-----the session type is set in the settings.py-------
                uid = uuid.uuid1().hex
                req.session['uid'] = uid
                user.uid = uid
                #print uid
                user.save()
                #print req.session.get('uid')
              
                #print rmbme                
                #response = render_to_response('index.html',{})
                return HttpResponseRedirect('/index/')
            
                ##----place userinfo into cookie----
                ##-----if the rmbme box is checked,set values into cookies-----
                if rmbme == 'rmbme':
                    response.set_cookie('username',account,2592000)
                    response.set_cookie('id',encrypted_password,2592000)
                return response
            else:
                #return HttpResponseRedirect('/')
                response = render_to_response('home.html',
                                            {'login_form':login_form,'status':status}
                                            ,context_instance=RequestContext(req))
                ##-----delete cookies-------
                ##-----prevent hacker edit the cookie,or cookie wrong----
                response.delete_cookie('username')
                response.delete_cookie('id')
                return response
            
    else:
        login_form = UserLoginForm()
            
    return render_to_response('home.html',{'login_form':login_form,'status':status},
                              context_instance=RequestContext(req))


#########################
#    vertify username   #
#########################
@csrf_exempt
def ver_signup(req):
    inputaccount = req.POST.get("name",None)
    fieldtype = req.POST.get("type",None)

    if fieldtype == "name":
        try:
            User.objects.get(name=inputaccount)
            return HttpResponse(json.dumps({"msg":"error"}))
        except:
            return HttpResponse(json.dumps({"msg":"success"}))
    elif fieldtype == "email":
        emailtype = __validateEmail(inputaccount)
        if emailtype == 0:
            return HttpResponse(json.dumps({"msg":"format error"}))
        try:
            User.objects.get(email=inputaccount)
            return HttpResponse(json.dumps({"msg":"error"}))
        except:
            return HttpResponse(json.dumps({"msg":"success"}))
   
    return HttpResponse(json.dumps({"msg":""}))


#####################
#      log out      #
#####################
def logout(req):
    ##---------delete the uid session--------
    ##----try there is no session before logging out------
    try:
        del req.session['uid']
    except:
        pass
    ##---------delete the coolie--------
    response = HttpResponseRedirect('/')
    response.delete_cookie('username')
    response.delete_cookie('id')
    return response

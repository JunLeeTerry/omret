__author__ = 'terry'
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
import json

from qiniu import Auth, put_file
import qiniu.config
from omret import settings
import uuid
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from omret.omretuser.views import hasUserSession, getUserFromSession
import base64

QINIU_BUCKET_DOMAIN = settings.QINIU_BUCKET_DOMAIN
ACCESS_KEY = settings.ACCESS_KEY
SECRET_KEY = settings.SECRET_KEY
BUKET_NAME = settings.BUKET_NAME

'''
def imageupload(req):
    q = Auth(ACCESS_KEY, SECRET_KEY)
    key = 'first.jpg'

    token = q.upload_token(BUKET_NAME, key, 3600)
    localfile = '/home/terry/first.jpg'
    ret, info = put_file(token, key, localfile)
    return HttpResponse(json.dumps({"url": QINIU_BUCKET_DOMAIN + key, "uptoken": token}))
'''


def token(req):
    q = Auth(ACCESS_KEY, SECRET_KEY)

    # key = uuid.uuid1()
    # print BUKET_NAME
    token = q.upload_token(BUKET_NAME)

    return HttpResponse(json.dumps({"uptoken": token}))


@csrf_exempt
def headupload(req):
    try:
        user = getUserFromSession(req)
    except Exception, e:
        return HttpResponseRedirect('/')

    file = req.POST.get('file', None)
    q = Auth(ACCESS_KEY, SECRET_KEY)
    key = "usrhead/"+str(uuid.uuid1())
    #key = "userhead/" + user.name
    token = q.upload_token(BUKET_NAME)

    # url = QINIU_BUCKET_DOMAIN+"putb64/20264"
    url = "http://up.qiniu.com/putb64/-1/key/" + base64.b64encode(key)
    print url
    # print 'file:'+str(file)

    return HttpResponse(json.dumps({"token": token, "url": url, "key": key}))


def recordhead(req):
    try:
        user = getUserFromSession(req)
    except Exception, e:
        return HttpResponseRedirect('/')

    key = req.GET.get('key')
    print key
    try:
        '''
        userheadimg = UserHeadImg.objects.get(user=user)
        userheadimg.url = QINIU_BUCKET_DOMAIN+key
        userheadimg.save()
        '''
        user.headurl = QINIU_BUCKET_DOMAIN+key
        user.save()
    except Exception,e:
        print e

    return HttpResponse(json.dumps({}))

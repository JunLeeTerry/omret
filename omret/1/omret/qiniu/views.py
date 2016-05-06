__author__ = 'terry'
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
import json

from qiniu import Auth, put_file
import qiniu.config
from omret import settings
import uuid
from django.views.decorators.csrf import csrf_protect,csrf_exempt


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
    q = Auth(ACCESS_KEY,SECRET_KEY)

    key = uuid.uuid1()
    #print BUKET_NAME
    token = q.upload_token(BUKET_NAME)

    return HttpResponse(json.dumps({"uptoken":token}))

@csrf_exempt
def headupload(req):
    file = req.POST.get('file',None)
    print 'file:'+str(file)

    return HttpResponse(json.dumps({}))
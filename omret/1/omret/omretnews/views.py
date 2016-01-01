#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from omret.logreg.models import User
from omret.omretnews.models import Topic,OmretNews
from omret.omretuser.views import hasUserSession,getUserFromSession
import datetime,time

# Create your views here.
def index(req):

    if not hasUserSession(req):
        return HttpResponseRedirect('/')
    
    ##-------if no session or cannot find user by session,turn to login page----
    user = getUserFromSession(req)  
    ##-------get all topics from sql--------
    topics = Topic.objects.all()    
    ##------get all omretnews from sql------
    news = OmretNews.objects.all()
    
    ##------compute the information of numbox-----
    numboxdata = []
    start = time.time()
    try:
        personnews = OmretNews.objects.filter(author=user.name)
        numboxdata = __comDataofNumbox(personnews)
    except:
        numboxdata = [0, 0, 0]
    end = time.time()
    #-----test the numboxdata and run time-----
    print str(numboxdata)+' run time:'+str(end-start)

    response = render_to_response('index.html',{'username':user.name,'topiclist':topics,'newslist':news,'numboxdata':numboxdata})
    return response


'''
caculate the number of numbox
@return [daynum,weeknum,monthnum]
[3,4,10],etc.
'''
def __comDataofNumbox(personnews):
    daynum = 0
    weeknum = 0
    monthnum = 0
    for personnew in personnews:
        _subtime = personnew.subtime
        _today = datetime.date.today()
        
        ##-----judge whether the new is in this month------
        if _subtime.year == _today.year and _subtime.month == _today.month:
            monthnum = monthnum + 1 
            ##-----judge whether the new is in this week------
            if _subtime.isocalendar()[1] == _today.isocalendar()[1]:
                weeknum = weeknum + 1
                ##------judge whether the new is in today------
                if _subtime.day == _today.day:
                    daynum = daynum + 1 
    print [daynum, weeknum, monthnum]
    return [daynum, weeknum, monthnum]
        
    

#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from omret.logreg.models import User
from omret.omretnews.models import Topic,OmretNews
from omret.omretuser.views import hasUserSession,getUserFromSession
from omret.omretnews.forms import NewsArtiForm
import datetime,time
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(req):
    
    ##-------if no session or cannot find user by session,turn to login page----
    if not hasUserSession(req):
        return HttpResponseRedirect('/')
    
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
        
##---------the page for posting artical--------
@csrf_protect
def postarti(req):
    ##-------if no session of user or can not find user by session then turn to login page
    if not hasUserSession(req):
        return HttpResponseRedirect('/')

    user = getUserFromSession(req)

    artiform = NewsArtiForm()
    ##------get post form data-------
    if req.method == 'POST':
        artiformPost = NewsArtiForm(req.POST)
        if artiformPost.is_valid():
            ##------postarti model-------
            title = artiformPost.cleaned_data['title']
            topic_name = artiformPost.cleaned_data['topic']
            ##------get topic by topic name-------
            try:
                topic = Topic.objects.get(name=topic_name)
            except Exception,e:
                print e
                topic = Topic.objects[0]

            content = artiformPost.cleaned_data['content']
            newsarti = OmretNews()
            __setNewsArti(newsarti,title,topic,content,user.name)

            ##-------if save artical successfully,return to index page--------
            ##-------if save error,stay in the postarti page and hint error message--------
            try:
                newsarti.save()
                return HttpResponseRedirect('/index/')
            except Exception,e:
                print e

    response = render_to_response('postarti.html',{'username':user.name,"artiform":artiform},context_instance=RequestContext(req))
    return response

'''
set valus to OmretNews model

author <=> user.name
'''
def __setNewsArti(newsarti,title,topic,content,author,upvotes=0,downvotes=0):
    newsarti.title = title
    newsarti.topic = topic
    newsarti.content = content
    newsarti.up_votes = upvotes
    newsarti.down_votes = downvotes
    newsarti.author = author

def artiindex(req,index):
    ##------get specific news by index--------
    new = OmretNews.objects.get(id=index)
    return HttpResponse(new.content);
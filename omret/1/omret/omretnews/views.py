# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from omret.logreg.models import User
from omret.omretnews.models import Topic, OmretNews, NewComments, NewCommentsChats, Notification
from omret.omretuser.views import hasUserSession, getUserFromSession
from omret.omretnews.forms import NewsArtiForm, NewQulicklyCommentForm, NewQulicklyChatForm
import omret.omretnews.models
import datetime, time
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
    ##------get topic list and num-------
    topicandNum = __comNumofTopic(news, topics)

    ##------compute the information of numbox-----
    numboxdata = []
    start = time.time()
    try:
        personnews = OmretNews.objects.filter(author=user)
        numboxdata = __comDataofNumbox(personnews)
    except:
        numboxdata = [0, 0, 0]
    end = time.time()
    # -----test the numboxdata and run time-----
    print str(numboxdata) + ' run time:' + str(end - start)

    response = render_to_response('index.html', {'username': user.name, 'topiclist': topicandNum, 'newslist': news,
                                                 'numboxdata': numboxdata}, context_instance=RequestContext(req))
    return response


'''
caculate the number of specific topic and the topic name
advance : reduce SQL query
@return [(topicname,topicnum)]
[[<Topic Object 1>,23],[<Topic Object 2>,50]]
'''


def __comNumofTopic(news, topics):
    topicnum = []
    # -------init topicnum list-------
    for topic in topics:
        topicnum.append([topic, 0])
    for topicnumindex in topicnum:
        for new in news:
            if new.topic.name == topicnumindex[0].name:
                topicnumindex[1] = topicnumindex[1] + 1
    return topicnum


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
    # print [daynum, weeknum, monthnum]
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
            except Exception, e:
                print e
                topic = Topic.objects[0]

            content = artiformPost.cleaned_data['content']
            newsarti = OmretNews()
            __setNewsArti(newsarti, title, topic, content, user)

            ##-------if save artical successfully,return to index page--------
            ##-------if save error,stay in the postarti page and hint error message--------
            try:
                newsarti.save()
                return HttpResponseRedirect('/index/')
            except Exception, e:
                print e

    response = render_to_response('postarti.html', {'username': user.name, "artiform": artiform},
                                  context_instance=RequestContext(req))
    return response


'''
set valus to OmretNews model

author <=> user.name
'''


def __setNewsArti(newsarti, title, topic, content, author, upvotes=0, downvotes=0):
    newsarti.title = title
    newsarti.topic = topic
    newsarti.content = content
    newsarti.up_votes = upvotes
    newsarti.down_votes = downvotes
    newsarti.author = author


def artiindex(req, index):
    ##-------if no session of user or can not find user by session then turn to login page
    if not hasUserSession(req):
        return HttpResponseRedirect('/')

    user = getUserFromSession(req)
    ##------get specific news by index--------
    new = OmretNews.objects.get(id=index)

    ##------quickly reply part--------
    ##------get quickly reply form object-------
    commentform = NewQulicklyCommentForm()
    chatform = NewQulicklyChatForm()
    if req.method == 'POST':
        ##------comment form post---------
        if req.POST.has_key('comment'):
            commentPost = NewQulicklyCommentForm(req.POST)
            if commentPost.is_valid():
                ##------get content of the arti's comment-------
                commentcontent = commentPost.cleaned_data['content']
                newcomment = NewComments()
                __setNewComment(newcomment, commentcontent, new, user)
                try:
                    ##----save comment-------
                    newcomment.save()
                    ##----save notification of arti owner------


                    return HttpResponseRedirect('/arti' + index)
                except Exception, e:
                    print e
        ##-------chat form post--------
        elif req.POST.has_key('chat'):
            chatPost = NewQulicklyChatForm(req.POST)
            if chatPost.is_valid():
                ##--------get content of comment's chat--------
                chatcontent = chatPost.cleaned_data['content']
                comment_id = req.POST.get('commentid')

                comment = NewComments.objects.get(id=comment_id)

                newcommentchat = NewCommentsChats()
                __setNewCommentChat(newcommentchat, comment, chatcontent, new, user)

                print chatcontent, comment_id
                try:
                    newcommentchat.save()
                    return HttpResponseRedirect('/arti' + index)
                except Exception, e:
                    print e


    ##------get all comments of the specific new----------
    comments = NewComments.objects.filter(article_id=index).order_by("-comment_time")
    chats = NewCommentsChats.objects.filter(article_id=index).order_by("-chat_time")
    commentchatList = __getCommentsChats(comments, chats)

    response = render_to_response('newindex.html', {'username': user.name, 'new': new, 'commentform': commentform,
                                                    'chatform': chatform, 'commentchatlist': commentchatList, },
                                  context_instance=RequestContext(req))

    return response


'''
set values into NewComment form

--------
article
user
commentcontent
--------
'''


def __setNewComment(comment, content, new, user):
    comment.comment_content = content
    comment.article = new
    comment.comment_user = user


'''
set values into NewCommentChat form

-------
article
comment
user
chatcontent
-------
'''


def __setNewCommentChat(chat, comment, content, new, user):
    chat.chat_content = content
    chat.article = new
    chat.comment = comment
    chat.chat_user = user


##---------get all Comments and Chats under the article---------
def __getCommentsChats(comments, chats):
    commentChatList = []
    tempchats = list(chats)
    for comment in comments:
        chatList = []
        for chat in tempchats:
            # print ('omretnews/__getCommentsChats'+str(chat.comment.id))
            if chat.comment.id == comment.id:
                chatList.append(chat)
                # tempchats.remove(chat)
        commentChatList.append([comment, chatList])

    # print commentChatList
    return commentChatList


'''
set values into Notification model

-------
user //the user is who need to notificate
article
type //arti reply or comment reply
-------
'''


def __setNotification(notification, user, arti, type):
    notification.user = user
    notification.article = arti
    notification.type = type

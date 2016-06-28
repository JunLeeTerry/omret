#-*- coding:utf-8 -*-
from django.db import models
import hashlib
from django.core.mail import send_mail,EmailMultiAlternatives
from pwencryption import pwEncryption
from sendEmailThread import EmailThread
from omret import settings

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50,unique = True)
    password = models.CharField(max_length=200)
    email = models.EmailField(blank=False,unique = True)
    headurl = models.CharField(max_length=3000,default=settings.DEFAULT_HEAD_URL)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if self.is_active == False:
            #self.password = hashlib.sha1(self.password).hexdigest()
            self.password = pwEncryption().encryptionByPasswd(self.password)
        #test password
        #print 'sql_password: '+self.password
        super(User,self).save(*args,**kwargs)

class UserActivationCode(models.Model):
    #name = models.CharField(max_length=50,unique = True)
    user = models.OneToOneField(User,unique = True)
    ##------activation code--------
    activation_code = models.CharField('activation code',max_length=200)

    def send_activation_email(self):
        ##------local environment---------
        subject,from_email,to_email = u'[Omret]activation url','omret@sina.com',self.user.email
        ##------test user email---------
        print self.user.email
        text_content = '点击下面的链接完成注册\n'
        ##------domain name address is sae----------
        #html_content = u'<a href="http://r305.sinaapp.com/validatemail/?username=%s&code=%s">http://r305.sinaapp.com/validatemail/?username=%s&code=%s</a>' % (self.user.name,self.activation_code,self.user.name,self.activation_code)
        ##------domain name address is localhost----------
        html_content = u'<h3>请点击下面的链接完成注册.<h3><br><a href="http://www.omret.com/validatemail/?username=%s&code=%s">http://www.omret.com/validatemail/?username=%s&code=%s</a>' % (self.user.name,self.activation_code,self.user.name,self.activation_code)
        msg = EmailMultiAlternatives(subject,text_content,from_email,[to_email])
        msg.attach_alternative(html_content,'text/html')
        EmailThread(msg).start()
    
      
    

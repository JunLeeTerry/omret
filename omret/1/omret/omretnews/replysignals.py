__author__ = 'terry'

import django.dispatch
from django.dispatch import receiver

class ReplySignals(object):

    global replySignal
    replySignal = django.dispatch.Signal(providing_args=['user'])

    @receiver(replySignal)
    def replysignal_callback(self, **kwargs):
        print "test signal"

__author__ = 'terry'

import django.dispatch
from django.dispatch import receiver


replySignal = django.dispatch.Signal(providing_args=['user'])


@receiver(replySignal)
def replysignal_callback(self, **kwargs):
    print "test signal"

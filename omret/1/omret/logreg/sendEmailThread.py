import threading

class EmailThread(threading.Thread):
    def __init__(self,msg):
        threading.Thread.__init__(self)
        self.msg = msg
        
    def run(self):
        self.msg.send()

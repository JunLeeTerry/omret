#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import MySQLdb

#reload(sys)
#sys.setdefaultencoding('utf-8')
topicdata = [(1,u'Technology','#003366'),(2,u'Games','#cccc33'),(3,u'Comic','#ff9900'),(4,u'Sports','#339933'),(5,u'Finance','#996633'),(6,u'Education','#993333')]

conn = MySQLdb.Connection(host="localhost",db="app_omret",user="root",passwd="n11dforeSPEED")

cursor = conn.cursor()

cursor.executemany("insert into omretnews_topic values (%s,%s,%s)",topicdata)

conn.commit()
cursor.close()
conn.close()

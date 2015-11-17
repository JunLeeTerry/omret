#!/usr/bin/env python
#-*-coding:utf-8-*-

#author:Terry Lee
#date:2015/11/16 
#
#description:this script is used to exec omret coding lines.
#usage:first param is dir path
#      second param is exclude files array
 
import os
 
TOTAL = 0 #total line number
FILENUM = 0 #total file number
 
class execLine(object):
 
    #----get all files path under the specified dir-----
    def run(self,dirPath,excludeFiles):
        for fileordir in os.listdir(dirPath):        
            path = os.path.join(dirPath,fileordir)
            if os.path.isfile(path):
 
                #----exclude the specified files------
                for excludeFile in excludeFiles:
                    if fileordir != excludeFile:
                        line = self.execFileLines(path)
                        global TOTAL
                        TOTAL += line
                        global FILENUM
                        FILENUM += 1
                        print str(FILENUM)+': [filename] '+fileordir+(' '*(50-len(fileordir)))+'[line] '+str(line)
                         
            elif os.path.isdir(path):
                #----if file is dir,use recursion----
                self.run(path,excludeFiles)
     
    #----exec the lines of file,execpt blank line----            
    def execFileLines(self,filepath):
        line = len([ln for ln in open(filepath, 'rt') if ln.strip()])
        return line
 
    def showTotal(self):
        print "\ntotal file number: "+str(FILENUM)+"\ntotal lines: "+str(TOTAL)
     
execLine = execLine()
execLine.run('./omret',['setting.py','test.py'])
execLine.showTotal()

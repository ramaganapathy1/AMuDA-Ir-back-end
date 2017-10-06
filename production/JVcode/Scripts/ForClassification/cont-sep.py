import sys
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os
import sys
client = MongoClient('mongodb://localhost:27017/')
db = client.ir
import random
#li=[]
#color=open("AllColors.txt","r")
doc1=[]
doc2=[]
edgeConWT=[]
edgeElaWT=[]
edgeStart=[]
edgeEnd=[]
path=os.getcwd()+"/JVcode/Scripts/ForClassification/"
for file in os.listdir(path):
    edgeElaWT = []
    edgeConWT = []
    edgeStart = []
    edgeEnd = []
    if file.endswith(".tab.scores"):
        fdTemp=open(path+file,"r")
       # fdOut=open("output/new/cont-"+file,"w+")
        for i1 in fdTemp:
             line=i1.split(" ")
             #print line
             edgeStart.append(line[0])
             edgeEnd.append(line[1])
             edgeConWT.append(float(line[2]))
             if(float(line[3]))>0:
                edgeElaWT.append(float(line[3]))
             else:
                edgeElaWT.append(0.0)
        for i in range(0,len(edgeConWT)):
            for j in range(0, len(edgeConWT)):
                if (j < (len(edgeConWT) - 1)):
                    if (edgeConWT[j] < edgeConWT[j + 1]):
                        temp = edgeConWT[j]
                        edgeConWT[j] = edgeConWT[j + 1]
                        edgeConWT[j + 1] = temp
                        temp2 = edgeStart[j]
                        edgeStart[j] = edgeStart[j + 1]
                        edgeStart[j + 1] = temp2
                        temp3 = edgeEnd[j]
                        edgeEnd[j] = edgeEnd[j + 1]
                        edgeEnd[j + 1] = temp3
        #print (edgeConWT)
        print (edgeEnd)
        t1 = []
        for k in range(0,5):
          #  t1 = []
            # t=str(edgeStart[k])+" "+str(edgeEnd[k])+" "+str(edgeConWT[k])+" "+str(edgeElaWT[k])+"\n"
            t1.append(edgeEnd[k])
        print ("for : ---> ",file[:-10] , 'pdf')
        results = db.rPaper.update({'filename': file[:-10] + 'pdf'}, {'$set': {'continuation': t1}})
        print (results)
        #st=raw_input("press to continue....")

print "DONE"
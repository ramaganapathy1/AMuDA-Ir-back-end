import sys
import os
import random
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os
import sys
client = MongoClient('mongodb://localhost:27017/')
db = client.ir
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
    print (file)
    if file.endswith(".tab.scores"):
        fdTemp=open(path+file,"r")
        #fdOut=open("output/new/elab-"+file,"w+")
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
        for i in range(0,len(edgeElaWT)):
            for j in range(0, len(edgeElaWT)):
                if (j < (len(edgeConWT) - 1)):
                    if (edgeElaWT[j] < edgeElaWT[j + 1]):
                        temp = edgeElaWT[j]
                        edgeElaWT[j] = edgeElaWT[j + 1]
                        edgeElaWT[j + 1] = temp
                        temp2 = edgeStart[j]
                        edgeStart[j] = edgeStart[j + 1]
                        edgeStart[j + 1] = temp2
                        temp3 = edgeEnd[j]
                        edgeEnd[j] = edgeEnd[j + 1]
                        edgeEnd[j + 1] = temp3
        print (edgeEnd,edgeElaWT)
        t2 = []
        for k in range(0,5):
            t2.append(edgeEnd[k])
        print("for => ",file)
        results=db.rPapers.update({'filename': file[:-10]+'pdf'}, {'$set': {'elaboration':t2}})
        print (results)
print "DONE"
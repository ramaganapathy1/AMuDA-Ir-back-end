import os
from flask import session
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.ir
path=os.getcwd()
path=path+"/JVcode/Scripts/ForClassification/outputFiles/"
nodes=[]
f=[]
for file1 in os.listdir(path):
    if file1.endswith(".lazy"):
        f.append(file1)
        nodes.append(file1[:-5])
print f
start=[]
end=[]
scores=[]
for i in f:
    fdOpen=open(path+i,"r")
    for j in fdOpen:
        line=j.split("\t")
        if(line[0]!="Src"):
            if float(line[3])>0.000:
                start.append(line[0][:-4])
                end.append(line[1][:-4])
                scores.append(float(line[3]))
avgScore=[]
#print scores
for i in range(0,len(nodes)):
    temp=0
    for j in range(0,len(start)):
        if nodes[i]==start[j]:
            #print "scores ",scores[j]
            temp=temp+float(scores[j])
#    print temp
    avgScore.append(float(temp))
for i in range(0,len(nodes)-1):
    for j in range(0,len(nodes)-1):
        if float(avgScore[j])<float(avgScore[j]):
            temp=""
            temp=nodes[j]
            nodes[j]=nodes[j+1]
            nodes[j+1]=temp
            temp=0
            temp=float(avgScore[j])
            avgScore[j]=float(avgScore[j+1])
            avgScore[j+1]=float(temp)
base=nodes[0]+".tab"
base1=base
print base
#print nodes,avgScore
#client = MongoClient('mongodb://localhost:27017/')
#db = client.ir
import os, sys

liststart = []
listend = []
final = []
for i in f:
    fd = open(path+i, "r")
    doca = []
    docb = []
    doc1 = []
    doc2 = []
    gain = []
    print "for ---- ", i
    for j in fd:
        line = j.split("\t")
        if line[0] != "Src":
            if line[2] > 0.0:
                gain.append(line[2])
                doc1.append(line[0])
                doc2.append(line[1])

    base = 0
    for k in range(0, len(doc1)):
        for l in range(0, len(doc1)):
            if doc1[k] == doc2[l]:
                base = gain[l]

    for k in range(1, len(doc1)):
        for j in range(1, len(doc2)):
            if (gain[j - 1] > gain[j]):
                t = gain[j - 1]
                gain[j - 1] = gain[j]
                gain[j] = t
                t = doc2[j - 1]
                doc2[j - 1] = doc2[j]
                doc2[j] = t
    c = 3
    pathFound=[]
    for k in range(0, len(doc1)):
        if c == 0:
            break
        if gain[k] > base:
            print doc2[k], "\t-----\t", gain[k]
            pathFound.append(doc2[k][:-3]+"pdf")
            if c == 3:
                liststart.append(i)
                listend.append(doc2[k])
            c -= 1
    print "base:\t", base, "\n"
    try:
        results = db.recom.insert_one({"_id": i[:-4] + "pdf","continuation": pathFound})
        print results
    except:
        results = db.recom.update({"_id": i[:-4] + "pdf"}, {'$set': {"continuation": pathFound}})
        print results
final = ["00000" for x in range(len(liststart))]
final[0] = base1

for i in range(1, len(final)):
    for j in range(0, len(liststart)):
        if final[i - 1][:-3] == liststart[j][:-4]:
            if (listend[j] in final):
                break
            else:
                final[i] = listend[j]
print final
li1=[]
for i in final:
    if i!='00000':
        li1.append(i)
rs=db.rPaper.find_one({'filename':base1[:-3]+"pdf"})
userId=rs['userId']
results = db.user.update({'_id':userId},{'$set':{"path":li1}})
print li1
print results


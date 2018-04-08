import sys
import os
import operator
from tree3 import *
from pymongo import MongoClient
from werkzeug import secure_filename
from datetime import datetime
import thread,time
import os
client = MongoClient('mongodb://localhost:27017/')
db = client.ir
path=os.getcwd()+"/JVcode/Scripts/ForClassification"
#path=os.getcwd()
def updateMongo(node,children):
    #domain=[]
    print node
    if children != "null":
        for i in range(0,len(children)):
            name1=children[i][:-10]+"pdf"
            print name1
            res=db.papers.find_one({'filename':name1})
            temp=[]
            temp.append(res['_id'])
            temp.append(res['domain'])
            children[i]=temp
            #domain.append(res['domain'])
    node=node[:-10]+"pdf"
    print "for ----",node,"  children ----",children
    res=db.papers.update_one({'filename':node},{'$set':{'continuation':children}})
    print res
def docReturn(name):
    fd=open(path+"/"+name+".scores","r")
    doc1=[]
    doc2=[]
    cont=[]
    toRet = []
    for i in fd:
        line=i.split()
        if name!=doc2:
            doc1.append(line[0])
            doc2.append(line[1])
            cont.append(float(line[2]))
    for i in range(0,len(cont)-1):
        for j in range(0,len(cont)-1):
            if float(cont[j])<float(cont[j+1]):
                temp=float(cont[j])
                cont[j]=float(cont[j+1])
                cont[j+1]=temp
                temp=doc2[j]
                doc2[j]=doc2[j+1]
                doc2[j+1]=temp
    for i in range(0,len(cont)):
        if cont[i] >= (0.3 * max(cont)):
            toRet.append(doc2[i])
    return toRet


"""def addtotree(tree,node,outdict):
    toAdd = []
    print "===============",node.v,"==========="
    for i in outdict[node.v]:
        stri = i+".scores"
        #print stri,"\t",tree.find(stri)
        if tree.find(stri) == None:
            toAdd.append(stri)
    print ":::::::::::::::::::::::::::::::::::::::::::::"
    if len(toAdd) != 0:
        tree.add(node.v,toAdd)
        tree.printTree()
        if (node.l != None):
            addtotree(tree,node.l,outdict)
        if (node.r != None):
            addtotree(tree,node.r,outdict)
    return tree"""

def addtotree2(tree,node,outdict):
    thislevel = [node]
    while thislevel:
        nextlevel = []
        for n in thislevel:
            print "===============",n.v,"==========="
            toAdd = []
            print outdict[n.v]
            for i in outdict[n.v]:
                stri = i+".scores"
                print stri,"\t",tree.find(stri)
                if tree.find(stri) == None:
                    toAdd.append(stri)
            print "To ADD::\n",toAdd
            if len(toAdd) != 0:
                tree.add(n.v,toAdd)
            print "check -----Parent ",n.v
            #print "\n\ncheck---------",n.v,n.l.v,n.r.v
            temp1=[]
            if n.l:
                nextlevel.append(n.l)
                print "check -----Left ",n.l.v
                temp1.append(n.l.v)
            if n.r: 
                nextlevel.append(n.r)
                print "check -----Right ",n.v
                temp1.append(n.r.v)
            if len(temp1)>0:
                updateMongo(n.v,temp1)
            else:
                updateMongo(n.v,"null")
            print "NEXTLEVEL\n",nextlevel
            print ":::::::::::::::::::::::::::::::::::::::::::::"
        thislevel = nextlevel
    return tree


path=os.getcwd()+"/JVcode/Scripts/ForClassification"
f=[]
for file1 in os.listdir(path):
    if file1.endswith(".tab.scores"):
        f.append(file1)

dict1=dict()
path1=os.getcwd()+"/JVcode/Scripts/ForClassification/"
for i in f:
    fd=open(path1+i,"r")
    dict1[i] = 0.0
    for j in fd:
        line = j.split()
        if float(line[2]) > 0.0:
            dict1[i] = dict1[i] + float(line[2])

outdict = dict()
for line in f:
    ret = docReturn(line[:-7])
    for j in ret:
        if j != line[:-7]:
            if line in outdict:
		if j+".scores" in f:
                    outdict[line].append(j)
            else:
                outdict[line] = [j]
"""
for i,j in outdict.items():
    print i,"\t",j
"""

basepaper =  max(dict1.iteritems(), key=operator.itemgetter(1))[0]
print "BASE PAPER :: ",basepaper

tree = Tree()
tree.addroot(basepaper)
node = tree.root

print "###########################################"
tree = addtotree2(tree,node,outdict)
print "###########################################"
print "###########################################"
print "###########################################"
print "\t\tFINAL TREE"
print "###########################################"
print "###########################################"
print "###########################################"
print node.v

fdout = open(path1+"tree.txt","w")
tree.prettyprint(node,"|__",fdout)
fdout.close()

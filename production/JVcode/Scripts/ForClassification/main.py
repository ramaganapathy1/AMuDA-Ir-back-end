import os
import numpy as np
import math
import scipy.stats
import matplotlib.pyplot as plt
from nltk.corpus import wordnet
import nltk

def plotGraph(start,end,wt):
    fdout=open("output.gdf","w+")
    keys=removeDuplicate(start)
    ini="nodedef> name,label"+'\n'
    fdout.write(ini)
    for i in range(0,len(f)):
        s="v"+str(i)+","+f[i][:-11]+"\n"
        fdout.write(s)
    fdout.write("edgedef> node1,node2,directed,weight,color,labelvisible\n")
    for i in range(0,len(edgeConWT)):
        if(float(wt[i])>0.0):
            entry="v"+str(f.index(start[i]))+",v"+str(f.index(end[i]))+",TRUE,"+str(wt[i])+",#FF0000,true\n"
        else:
            entry="v"+str(f.index(start[i]))+",v"+str(f.index(end[i]))+",TRUE,"+str(abs(wt[i]))+",#228B22,true\n"
        fdout.write(entry)

def removeDuplicate(li):
    dup=[]
    l=[]
    for i in li:
        if i not in dup:
            dup.append(i)
            l.append(i)
    return l

def synonyms(word):
    syn=wordnet.synsets(word)
    for i in range(0,len(syn)):
        syn[i]=str(syn[i].lemmas()[0].name())
    if(len(syn)>0):
        print removeDuplicate(syn)
    else:
        return []

def gini(p):
    sum1=0
    for p1 in p:
        sum1+=(p1*p1)
    return 1-sum1

def entropy(p):
    sum1 = 0
    for p1 in p:
        if(p1 != 0):
            diff = math.log10(p1) - math.log10(2)
            sum1+=(p1*diff)
    return -sum1

f=[]
edgeConWT=[]
edgeStart=[]
edgeEnd=[]
gain=[]
doc=[]
l=[]
base=0
path=os.getcwd()+"/JVcode/Scripts/ForClassification"
pathForTab=os.getcwd()+"/JVcode/Scripts/newtab"
outputPath=os.getcwd()+"/JVcode/Scripts/ForClassification/outputFiles/"
for file1 in os.listdir(path):
    if file1.endswith(".tab.scores"):
            f.append(file1)
print len(f)

for f1 in range(len(f)):
    src=f[f1]
    src1=src[:-7]
    #print src1
    fd1=open(path+"/"+src)
    l=[]
    doc=[]
    for i in fd1:
      li=i.split(" ")
      l.append(li[2])
      doc.append(li[1])
      print li[1]
    gain=[]
    for i in range(1,len(doc)):
        for j in range(1,len(doc)):
            if(l[j-1]<l[j]):
                t=l[j-1]
                l[j-1]=l[j]
                l[j]=t
                t=doc[j-1]
                doc[j-1]=doc[j]
                doc[j]=t
    print doc
    fdOut=open(outputPath+src1[:-3]+"lazy","w+")
    fdOut.write("Src\tDst\tGain\tCont-Score\n")
    for i0 in range(0,len(f)):
        print i0
        print src1 , doc
        fd1=open(pathForTab+"/"+src1,"r")
        fd2=open(pathForTab+"/"+doc[i0],"r")
        key1=[]
        tfidfDoc1=[]
        tfidfDoc2=[]
        cscoreDoc1=[]
        cscoreDoc2=[]
        commonDoc1Cscore =[]
        commonDoc2Cscore =[]
        commonDoc1Tfidf =[]
        commonDoc2Tfidf=[]
        commonDoc1Dispersion=[]
        commonDoc2Dispersion=[]
        dispersionDoc1=[]
        dispersionDoc2=[]
        key2=[]
        for i in fd1:
            i1=i.split("\t")
            key1.append(i1[0])
            tfidfDoc1.append(i1[1])
            cscoreDoc1.append(i1[3])
            dispersionDoc1.append(i1[2])
        for i in fd2:
            i1=i.split("\t")
            key2.append(i1[0])
            tfidfDoc2.append(i1[1])
            cscoreDoc2.append(i1[3])
            dispersionDoc2.append(i1[2])
        c=0
        e=[]
        x=[]
        x1=[]
        y1=[]
        tempTfidf=0
        tempCscore=0

        for i in range(3,len(key1)):
            for j in range(3,len(key2)):
		try:
			if key1[i]==key2[j]:
				commonDoc2Tfidf.append(float(tfidfDoc2[j]))
			      	commonDoc1Tfidf.append(float(tfidfDoc1[i]))
			    	commonDoc1Cscore.append(float(cscoreDoc1[i]))
			    	commonDoc2Cscore.append(float(cscoreDoc2[j]))	
			    	commonDoc1Dispersion.append(float(dispersionDoc1[i]))
				commonDoc2Dispersion.append(float(dispersionDoc2[j]))	    	
		except ValueError,e:
			print "error",e,"on line",i
	        """syn=[]
	        syn=synonyms(key1[i])
	        if(len(syn)>0):
	            syn=removeDuplicate(syn)
	            for k in syn:
	                for m in range(0,len(key2)):
	                    if k in removeDuplicate(synonyms(key2[m])):
	                         commonDoc2Tfidf[i]=commonDoc2Tfidf+tfidfDoc2[m]
	                         commonDoc2Cscore[i]=commonDoc2Cscore+cscoreDoc2[m]
	                         commonDoc2Dispersion[i]=commonDoc2Dispersion[i]+dispersionDoc2[m]
	        c=c+1
		"""

        eBefore=[]
        e=[]
        for i in range(0,len(commonDoc1Tfidf)):
            eBefore.append( ( 0.5*commonDoc1Tfidf[i]+commonDoc1Cscore[i] + commonDoc1Dispersion[i] ) )
        t1 = sum(eBefore)
	for i in range(0,len(eBefore)):
            if(t1 != 0):
		e.append(eBefore[i]/t1)
	    else:
		e.append(0)

        y1Before=[]
        y1=[]
        for i in range(0,len(commonDoc2Tfidf)):
            y1Before.append( (commonDoc2Cscore[i]+0.5*commonDoc2Tfidf[i] + commonDoc2Dispersion[i] ) )
        t2 = sum(y1Before)
        for i in range(0,len(y1Before)):
            if(t2 != 0):
		y1.append(y1Before[i]/t2)
	    else:
		y1.append(0)

        overall=0
        doc2=0
        overallgain=scipy.stats.entropy(e,None,2)
        doc2gain=scipy.stats.entropy(y1,None,2)
        gain1=doc2gain-overallgain

        if float(gain1)>0.0:
            value=(0.6*float(l[i0]))+(0.4*(5 - abs(overallgain-doc2gain)))
        else:
            value=(0.6*float(l[i0]))+(0.3*(5 - abs(overallgain-doc2gain)))
        print i0," -->\tBetween ",src," and ",doc[i0], "\t\tGain : ",value
	#print " over ", overallgain,"\t\tdoc2 : ",doc2gain,"\t\tCont : ",float(l[i0])
        fdOut.write(str(src1)+"\t"+str(doc[i0])+"\t"+str(value)+"\t"+str(l[i0])+"\t"+str(gain1)+"\n")

        if src1==doc[i0]:
            base=value

        if float(value)>0.0:
            edgeConWT.append(value)
            edgeStart.append(src)
            edgeEnd.append(doc[i0]+".scores")
        else:
            edgeConWT.append(value)
            edgeEnd.append(src)
            edgeStart.append(doc[i0]+".scores")

#print "\n",f[0],"\n"

import sys
import os
import random
li=[]
#color=open("AllColors.txt","r")
fdFinal=open("output-cont.gdf","w+")
doc1=[]
doc2=[]
edgeConWT=[]
edgeElaWT=[]
edgeStart=[]
edgeEnd=[]
for file in os.listdir(os.getcwd()):
    if file.endswith(".tab.scores"):
        fdTemp=open(file,"r")
        for i in fdTemp:
        	 line=i.split(" ")
        	 #print line
        	 edgeStart.append(line[0])
        	 edgeEnd.append(line[1])
        	 if(line[0] not in doc1):
        	 	doc1.append(line[0])
        	 if(line[1] not in doc2):
        	 	doc2.append(line[1])
        	 
        	 edgeConWT.append(float(line[2]))
           	 edgeElaWT.append(float(line[3]))
       
print "Start nodes = ",len(doc1)
print "End Nodes   = ",len(doc2)
print "Continuation Edge Count = ",len(edgeConWT)
print "Elaboration Edge Count  = ",len(edgeElaWT)

#normailzzation

maxC=max(edgeConWT)
minC=min(edgeConWT)

for i in range(0,len(edgeConWT)):
	edgeConWT[i]=(float((edgeConWT[i]-minC)/(maxC-minC)))
print edgeConWT

print max(edgeConWT)," ",min(edgeConWT)

maxE=max(edgeElaWT)
minE=min(edgeElaWT)


for i in range(0,len(edgeElaWT)):
	if(edgeElaWT[i]>0.0):
		edgeElaWT[i]=(float((edgeElaWT[i]-minE)/(maxE-minE)))
	else:
		edgeElaWT[i]=0.0
print edgeElaWT
print max(edgeElaWT)," ",min(edgeElaWT)

fdFinal.write("nodedef> name,label\n")

count=0
for i in doc1:
	t='v'+str(count)+','+str(i[:-4])+'\n'
	count=count+1
	fdFinal.write(t)

fdFinal.write("edgedef> node1,node2,directed,weight,color,labelvisible\n")
for i in range(0,len(edgeConWT)):
	if(edgeConWT[i]>(1.0*edgeElaWT[i])):
		if doc1.index(edgeStart[i])!=doc1.index(edgeEnd[i]):
			t="v"+str(doc1.index(edgeStart[i]))+",v"+str(doc1.index(edgeEnd[i]))+",true,"+str(edgeConWT[i])+",#FF0000,true\n" #red	
			fdFinal.write(t)
	else:
		t="v"+str(doc1.index(edgeStart[i]))+",v"+str(doc1.index(edgeEnd[i]))+",true,"+str(edgeElaWT[i])+",#228B22,true\n"	#green
		fdFinal.write(t)

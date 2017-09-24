import os
import math

listOfFiles = []

#for eachfile in os.listdir(os.getcwd()+"/tabfiles"): #tabfiles - folder with original tabfiles
for eachfile in os.listdir(os.getcwd()+"/tabfiles"):
    #if(eachfile.endswith(".tabn")):
    if(eachfile.endswith(".tab")):
        listOfFiles.append(eachfile)

def getcommongrams(name1, name2, docwrite):
    commonLambda = []
    splitTabDir = os.getcwd()+"/splitTabFiles/"
    doc11 = open(splitTabDir+name1+".four","r")
    doc12 = open(splitTabDir+name1+".three","r")
    doc13 = open(splitTabDir+name1+".two","r")
    doc14 = open(splitTabDir+name1+".one","r")
    doc21 = open(splitTabDir+name2+".four","r")
    doc22 = open(splitTabDir+name2+".three","r")
    doc23 = open(splitTabDir+name2+".two","r")
    doc24 = open(splitTabDir+name2+".one","r")
    onefile = [doc11,doc12,doc13,doc14]
    otherfile = [doc21,doc22,doc23,doc24]
    dsim = 0
    tsim = 0
    csim = 0
    for i in range(4):
        for eachline in onefile[i]:
            list1=eachline.split('\t')
            
            try:
                for everyline in otherfile[i]:
                    list2=everyline.split('\t')
                    try:
                        if list1[0]==list2[0]:
                            dsim = dsim + (1-math.fabs(float(list1[2]) - float(list2[2]))) 
                            print math.fabs(float(list1[2]) - float(list2[2]))
                            tsim = tsim + (float(list1[1]) - float(list2[1]))
                            csim = csim + (float(list1[3]) - float(list2[3]))
            	    except ValueError:
			continue
                otherfile[i].seek(0)
            except ValueError:
                continue
    docwrite.write(name2+"\t"+str(dsim)+"\t"+str(tsim)+"\t"+str(csim)+"\t\n")
    
for eachFile in listOfFiles:
	docwrite = open(os.getcwd()+"/diffs/"+eachFile,"w")
	docwrite.write("name\td-sim\tt-diff\tc-diff\n")
	for everyfile in listOfFiles:
		getcommongrams(eachFile, everyfile, docwrite)
	docwrite.close()

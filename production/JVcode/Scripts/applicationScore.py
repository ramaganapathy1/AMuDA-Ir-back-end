import sys
import math
import os
path=os.getcwd()+"/production/JVcode/Scripts"
def getcommongrams(name1, name2):
    commonLambda = []
    tfidfs = []
    doc11 = open(name1+".four","r")
    doc12 = open(name1+".three","r")
    doc13 = open(name1+".two","r")
    doc14 = open(name1+".one","r")
    doc21 = open(name2+".four","r")
    doc22 = open(name2+".three","r")
    doc23 = open(name2+".two","r")
    doc24 = open(name2+".one","r")
    onefile = [doc11,doc12,doc13,doc14]
    otherfile = [doc21,doc22,doc23,doc24]
    for i in range(4):
        for eachline in onefile[i]:
            list1=eachline.split('\t')
            try:
                if float(list1[5])!=0 and float(list1[4])>0:
                    for everyline in otherfile[i]:
                        list2=everyline.split('\t')
                        try:
                            if list1[0]==list2[0] and float(list1[4])-float(list2[4])>0:
                            	commonLambda.append(float(list1[5])-float(list2[5]))
                        except ValueError:
                            continue
                    otherfile[i].seek(0)
            except ValueError:
                continue
    aggLambda = math.fsum(commonLambda)
    return aggLambda

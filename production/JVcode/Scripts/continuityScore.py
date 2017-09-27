import os
import math
path=os.getcwd()+"/JVcode/Scripts/splitTabFiles"
def getcommongrams(name1, name2):
	goodLambda = []
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
				if float(list1[1])!=0:
					if float(list1[2])!=0:
						for everyline in otherfile[i]:
							list2=everyline.split('\t')
							try:
								if list1[0]==list2[0]:
									#sim = 50 - math.fabs(float(list1[2])-float(list2[2]))
									#sim = 1 - math.fabs(float(list1[2])-float(list2[2]))
									sim = 1 - (float(list1[2])-float(list2[2]))
									minTF = min(float(list1[1]),float(list2[1]))
									score = sim*minTF
									#if sim>=48:
									if sim>=0:
										if sim<=2:
											if minTF>=0.002:
												goodLambda.append(score*1.3)
									else:
										goodLambda.append(score)
									#goodLambda.append(score)
							except ValueError:
								continue
						otherfile[i].seek(0)
			except ValueError:
				continue
	if len(goodLambda)!=0:
		gAvg = math.fsum(goodLambda)/len(goodLambda)
		return gAvg
	else:
		return 0

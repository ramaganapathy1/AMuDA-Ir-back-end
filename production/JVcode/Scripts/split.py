import os
path=os.getcwd()+"/JVcode/Scripts"
files = os.listdir(path+"/tabfiles")
for eachfile in files:
	#if eachfile.endswith(".tabn"):
	if(eachfile.endswith(".tab")):
		doc = open(path+"/tabfiles/"+eachfile,"r")
		#doc = open(os.getcwd()+"/home/ramyananth/Desktop/research work/tab files"+eachfile,"r")
		doc1 = open(path+"/splitTabFiles/"+eachfile+".one","w") #output folder
		doc2 = open(path+"/splitTabFiles/"+eachfile+".two","w")
		doc3 = open(path+"/splitTabFiles/"+eachfile+".three","w")
		doc4 = open(path+"/splitTabFiles/"+eachfile+".four","w")
		for everyline in doc:
			try:
				thisline = everyline.split('\t')
				n = thisline[0].count(' ')
				if n == 3:
					doc4.write(str(everyline))
				elif n == 2:
					doc3.write(str(everyline))
				elif n == 1:
					doc2.write(str(everyline))
				elif n == 0:
					doc1.write(str(everyline))
			except ValueError:
				continue
		doc1.close();
		doc2.close();
		doc3.close();
		doc4.close();
		doc.close();
import os
#files = os.listdir(os.getcwd()+"/tabfiles") # source folder
#files = os.listdir("/home/ramyananth/Desktop/RAMA IR/JV")
files = os.listdir(os.getcwd()+"/tabfiles")
for eachfile in files:
	#if eachfile.endswith(".tabn"):
	if(eachfile.endswith(".tab")):
		doc = open(os.getcwd()+"/tabfiles/"+eachfile,"r")
		#doc = open(os.getcwd()+"/home/ramyananth/Desktop/research work/tab files"+eachfile,"r")
		doc1 = open(os.getcwd()+"/splitTabFiles/"+eachfile+".one","w") #output folder
		doc2 = open(os.getcwd()+"/splitTabFiles/"+eachfile+".two","w")
		doc3 = open(os.getcwd()+"/splitTabFiles/"+eachfile+".three","w")
		doc4 = open(os.getcwd()+"/splitTabFiles/"+eachfile+".four","w")
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
			
			

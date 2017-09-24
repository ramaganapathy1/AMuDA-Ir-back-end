import os

listOfFiles = os.listdir(os.getcwd()+"/tabfiles")
for filename in listOfFiles:
	print filename
	doc=open(filename)
	print doc.read()
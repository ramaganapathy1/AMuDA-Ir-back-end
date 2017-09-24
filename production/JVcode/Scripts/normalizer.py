import os

#listOfFiles = os.listdir(os.getcwd()+"/tabfiles")

highestT = 0.0
highestD = 0.0
highestC = 0.0

for filename in os.listdir(os.getcwd()):
	if filename.endswith(".tab"):
		doc = open(filename,"r")
		for line in doc:
			elements = line.split("\t")
			tfidf = float(elements[1])
			cscore = float(elements[3])
			dspan = float(elements[2])
			if tfidf >= highestT:
				highestT = tfidf
			if cscore >= highestC:
				highestC = cscore
			if dspan >= highestD:
				highestD = dspan
		doc.close()
		
print highestT,"\t", highestD,"\t", highestC,"\n"

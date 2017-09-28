#Sample Command: python grams.py ds8.txt "/var/www/metadata/output/preprocess_audio" "/var/www/metadata/output/preprocess_audio" 4
import sys
from stop_words import stopword
import os
import nltk
from nltk import stem

class gram:
	def __init__(self,file_name,input_folder,output_folder,complete_file_name,max_gram,gram_ext):
		self.doc_name=complete_file_name
		print self.doc_name
		#print self.doc_name
		self.grams={}
		f=open(self.doc_name,"r")
		self.max_gram=max_gram
		self.tokens=f.read()
		#print self.tokens
		self.tarray=self.tokens.split()
		#print self.tarray
		self.size=len(self.tarray)
		self.result_file=file_name.split("_")[0]+gram_ext
		self.result=output_folder+"/"+self.result_file
		#(self.doc_name).split("/")[1]
		#self.result="result/"+self.result.split(".")[0]+".grams"
		#self.one_g="result/"+self.result.split(".")[0]+".onegrams"
		self.final_grams=[]
	

	def extract_gram(self,n):
		t=[]
		tg=[]
		#global grams
		for i in range(len(self.tarray)-n):
			flag=0
			d=""
			token=[]
			tag=[]
			for j in range(n):
				token.append(self.tarray[i+j].split("/")[0])
				tag.append(self.tarray[i+j].split("/")[1])
				if (not is_number(token[j]) and token[j]!=" " and token[j]!=""):
					d=d+token[j]+" "
				else:
					flag=1
					break
			d=d.rstrip(" ")
			word=d.split()
			l=len(word)
			if ((flag==0) and (word[0].strip() not in stopword) and (word[l-1].strip() not in stopword) and (len(word[0])>2) and (len(word[l-1])>2)):
				try:
					self.grams[d]+=1
				except:
					self.grams[d]=1
			

	
	def display(self):
		f=open(self.result,"w")
		count=0
		#fone=open(self.one_g,"w")
		#f.write(self.doc_name+"\n")
		for k in (self.grams).keys():
		#	if self.grams[k]>1:						
			f.write(k.replace("'","")+"\n")
		f.close()
		os.system('chmod 777 '+self.result)
			

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def repeated(token):
	cnt={}
	repeat=0
	for word in token:
		try:
			cnt[word]+=1
			repeat=1
			break
		except:
			cnt[word]=1
	return repeat

def stem_token(stemmer_name,stopword):
	if stemmer_name=="Porter-Stemmer":
		#print ("Performing Porter Stemming")
		stemmer = stem.PorterStemmer()
		for count in range(len(stopword)):
			stopword[count]=stemmer.stem(stopword[count])
	elif stemmer_name=="Lancaster-Stemmer":
		#print ("Performing Lancaster Stemming")
		stemmer = stem.LancasterStemmer()
		for count in range(len(stopword)):
			stopword[count]=stemmer.stem(stopword[count])
	elif stemmer_name=="WordNet-Lemmatizer":
		#print ("Performing Wordnet Lemmatization")
		stemmer = WordNetLemmatizer()
		for count in range(len(stopword)):
			stopword[count]=stemmer.lemmatize(stopword[count])
	return(stopword)



doc_grams=[]
not_noun=[]
doc_count=0

try:
	file_name=sys.argv[1]
	file_name_list=file_name.split(".")
	file_name=file_name_list[0]+"_tagged.txt"
	#print file_name
	#input_folder=sys.argv[2]
	input_folder="production/keyphrase/output"
	#print input_folder
	#lecture=explode(".",file_name)
	complete_file_name=input_folder+"/"+file_name
	#print complete_file_name
	#output_folder=sys.argv[3]
	output_folder="production/keyphrase/output"
	#print output_folder	
	max_gram=int(sys.argv[2])
	#print max_gram
	stemmer_name=sys.argv[3]
	gram_ext="_grams.txt"

except:
	print "No argument"
	sys.exit()
	#files=os.listdir("formal testing tagged transcript")
	#doc_count=0
	#doc=[]
	#for i in range(len(files)): 
	#	if files[i].endswith(".txt"):
	#		doc.append("formal testing tagged transcript/"+files[i])


stopword=stem_token(stemmer_name,stopword)
g=gram(file_name,input_folder,output_folder,complete_file_name,max_gram,gram_ext)
for i in range(max_gram,0,-1): 
	#print i
	g.extract_gram(i)
#g.extract_gram(2)
#g.extract_gram(1)
g.display()
#print "N grams extracted for"+g.doc_name
#os.system('rm '+g.doc_name)
#os.system('mv '+g.result+' '+g.doc_name)
#print len(doc_grams[d].grams),len(doc_grams[d].grams),"\n"
#print doc_grams[d].grams
#print "\n"

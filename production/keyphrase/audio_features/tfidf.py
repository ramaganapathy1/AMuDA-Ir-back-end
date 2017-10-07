#from disp import doc
import math
import sys
from operator import itemgetter
from stop_words import stopword
import math
from nltk import stem
import os
from stem import *

global doc_count

class tfidf:
    def __init__(self,doc_name,input_folder,output_folder,max_gram,result_ext,ext):
        self.name=doc_name
        self.doc_name=input_folder+"/"+doc_name
        self.grams={}
        f=open(self.doc_name,"r")
        self.max_gram=int(max_gram)
        self.tokens=f.read()
        self.tarray=self.tokens.split()
        self.size=len(self.tarray)
        self.result_file=doc_name.split(".")[0]+ext
        self.result=output_folder+"/"+self.result_file
        self.final_grams=[]
        self.idf={}
        self.tf_idf={}
    
    
    def getgramsfreq(self):
        #print "MAX_grams",self.max_gram
        #print self.doc_name
        #print len(self.tarray)
        t=[]
        tg=[]
        #global grams
        for i in range(len(self.tarray)-self.max_gram):
            for k in range(1,self.max_gram):
                flag=0
                d=""
                token=[]
                tag=[]
                for j in range(k):
                    #print "self.tarray" , self.tarray[i+j]
                    token.append(self.tarray[i+j].split("/")[0])
                    if (not is_number(token[j]) and token[j]!=" " and token[j]!=""):
                        d=d+token[j]+" "
                    else:
                        flag=1
                        break
                d=d.rstrip(" ")
                word=d.split()
                word1=""
                for w in word:
                        w=w.lower()
                        w=w.strip(".")
                        w=w.strip(",")
                        w=w.strip(")")
                        w=w.strip("(")
                        w=w.strip("{")
                        w=w.strip("}")
                        w=w.strip("[")
                        w=w.strip("]")
                        w=w.strip(":")
                        w=w.strip("-")
                        w=w.strip(" ")
                        w=w.strip("()")
                        w=w.strip('"')
                        w=w.strip("'")
                        word1=word1+w+" "
                    
                word1=word1.rstrip(" ")
                word1=word1.lstrip(" ")
                word=word1.split()
                l=len(word)
                if ( len(word)>0 and (flag==0) and (word[0].strip() not in stopword) and (word[l-1].strip() not in stopword) and (len(word[0])>2) and (len(word[l-1])>2) ):
                    d=stem_token(word1)
                    try:
                        self.grams[d]+=1
                    except:
                        self.grams[d]=1
            
    
    def find_tfidf(self):
        print self.doc_name
        for t in self.grams.keys():
            t=t.lower()
            res=0
            for dd in document:
                if t in dd.grams.keys():
                    res=res+1
            try:
                #self.idf[t]=float(doc_count)/(float(1)+float(res))
                #self.tf_idf[t]=float(self.grams[t])*float(self.idf[t]);
                self.idf[t]=math.log(float(doc_count) /  float(res))
                self.tf_idf[t]=(len(t.split(" ")))*(float(self.grams[t])/float(self.size))*float(self.idf[t])
                if t == "amino acid":
                    print "len of the document" , self.size
                    print t,  self.tf_idf[t],  float(self.grams[t])/float(self.size),  float(self.idf[t]),  float(doc_count),  float(res)
            except:
                nothing=0
    
    def display(self):
        items=self.tf_idf.items()
        items.sort(key=itemgetter(1),reverse=True)
        f=open(self.result,"w")
        maxx=items[0][1]
        for i,t in items:
            f.write(str(i)+"::"+str(t)+"\n")
        f.close()
        os.system('chmod 777 '+self.result)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def stem_token(word):
	stem_token=""
	if stemmer_name=="Porter-Stemmer":
		#print ("Performing Porter Stemming")
		stemmer = stem.PorterStemmer()
		phrase_array_token=word.split()
		stem_token=""
		for s in phrase_array_token:
			stem_token=stem_token+stemmer.stem(s)+" "
		stem_token=stem_token.strip(" ")
		word=stem_token
	elif stemmer_name=="Lancaster-Stemmer":
		#print ("Performing Lancaster Stemming")
		stemmer = stem.LancasterStemmer()
		phrase_array_token=word.split()
		stem_token=""
		for s in phrase_array_token:
			stem_token=stem_token+stemmer.stem(s)+" "
		stem_token=stem_token.strip(" ")
		word=stem_token
	elif stemmer_name=="WordNet-Lemmatizer":
		#print ("Performing Wordnet Lemmatization")
		stemmer = stem.WordNetLemmatizer()
		phrase_array_token=word.split()
		stem_token=""
		for s in phrase_array_token:
			stem_token=stem_token+stemmer.lemmatize(s)+" "
		stem_token=stem_token.strip(" ")
		word=stem_token
			#stopword[count]=stemmer.lemmatize(stopword[count])
	return(word)

document=[]
doc_count=0
try:
	global stemmer_name
	#transcript_folder=sys.argv[1]
	transcript_folder="keyphrase/transcript"
	#grams_folder=sys.argv[2]
	grams_folder="keyphrase/output"
	stemmer_name=sys.argv[1]
	max_gram=int(sys.argv[2])
	#result_ext=sys.argv[5]
	result_ext="_tfidf.txt"
	#ext=sys.argv[6]
	ext="_tfidf.txt"
	video_file=sys.argv[3]; print "-----------------------------------", video_file
	key_file=""
	"""if len(sys.argv)-1>7:
		key_file=sys.argv[8]
	else:
		key_file="" """

except:
	print "No mandatory arguments"
	sys.exit()

doc_gram=[]

if os.path.isdir(transcript_folder):
	documents=os.listdir(transcript_folder)
	for d in documents:
		if d.endswith(".txt"):
			doc_gram.append(d)

for d in doc_gram:
	document.append(tfidf(d,transcript_folder,grams_folder,max_gram,result_ext,ext))
	doc_count+=1

for d in document:
	d.getgramsfreq(); print "done"

#testing_files= ["Basic-Electronics-Lec1.txt","Basic-Electronics-Lec2.txt","Basic-Electronics-Lec3.txt","Basic-Electronics-Lec4.txt","Basic-Electronics-Lec5.txt","Basic-Electronics-Lec6.txt","co-lec-3.txt","co-lec-12.txt","co-lec-13.txt","co-lec-14.txt","co-lec-15.txt","co-lec-16.txt","co-lec-17.txt","co-lec-18.txt","co-lec-19.txt","dbms-db21.txt","dbms-db22.txt","dbms-db24.txt","dbms-db25.txt","dbms-db26.txt","dbms-DBMS-introduction-lecture-1.txt","dbms-DBMS-lecture-2.txt","dbms-lec12.txt","dbms-lec14.txt","dbms-lec18.txt","Discrete-Lec-5.txt","Discrete-Lec-6.txt","Discrete-Lec-7.txt","Discrete-Lec-8.txt","iit-d-cg-Computer-Graphics-6.txt","iit-d-cg-Computer-Graphics-7.txt","iit-d-cg-Computer-Graphics-8.txt","iit-d-cg-Computer-Graphics-9.txt","iit-d-cg-Computer-Graphics-10.txt","iit-d-ppl-Lec-6.txt","iit-d-ppl-Lec-7.txt","iit-d-ppl-Lec-8.txt","iit-d-ppl-Lec-9.txt","iit-d-ppl-Lec-10.txt","iit-d-ppl-Lecture-11.txt","iit-d-ppl-Lecture-12.txt","iit-d-ppl-Lecture-13.txt","iit-d-ppl-Lecture-14.txt","iit-d-ppl-Lecture-15.txt","iit-d-ppl-Lecture-16.txt","iit-d-ppl-Lecture-17.txt","iit-k-psp-Ipsp-lec1.txt","iit-k-psp-Ipsp-lec2.txt","iit-k-psp-Ipsp-lec6.txt","iit-k-psp-Ipsp-lec7.txt","iit-k-psp-Ipsp-lec8.txt","iit-k-psp-Ipsp-lec9.txt","iit-k-psp-Ipsp-lec10.txt","iit-k-psp-lec-11.txt","iit-k-psp-lec-12.txt","iit-k-psp-lec-13.txt","Measurements-lec-1.txt","Measurements-lec-2.txt","Measurements-lec-3.txt","Measurements-lec-4.txt","Measurements-lec-5.txt","Measurements-lec-6.txt","nmplec1.txt","nmplec2.txt","nmplec3.txt","nmplec4.txt","nmplec5.txt","nmplec6.txt","nmplec7.txt","nmplec8.txt","nmplec9.txt","nmplec10.txt","nmplec12.txt","robotics-Am-lec7.txt","system-analysis-and-design-lect3.txt","system-analysis-and-design-lect5.txt","system-analysis-and-design-lect6.txt","system-analysis-and-design-lect12.txt"]
testing_files=[video_file]
#testing_files=["bio1.txt","cg2.txt","cg3.txt","cg4.txt","cg5.txt","CG1.txt","comparch1.txt","dbms1.txt","ds1.txt","ds2.txt","ds3.txt","ds4.txt","ds5.txt","ds6.txt","ds7.txt","ds8.txt","iit-d-ca-CA-LEC-2.txt","iit-d-ca-CA-LEC-4.txt","iit-d-ca-CA-LEC-5.txt","iit-d-ca-CA-LEC-6.txt","ppl1.txt","ppl2.txt","ppl3.txt","ppl4.txt"]
#testing_files=["ds10.txt", "ds11.txt", "embsys.txt", "it1.txt", "ppl5.txt"]

#testing_files= ["ds14.txt","ds15.txt","ds16.txt","ds17.txt","ds18.txt","ds19.txt","ds20.txt","ds29.txt","ds30.txt","ds31.txt","ds32.txt","ds33.txt","ds34.txt","ds35.txt","ds36.txt","ds21.txt","ds22.txt","ds23.txt","ds24.txt","ds25.txt","ds26.txt","ds27.txt","ds28.txt"]

for d in document:
	#d.find_tfidf()
	if d.name in testing_files:
		print d.name
		d.find_tfidf()
		d.display()

def write_tfidf_keys(result):
	print "Writing tf_idf"+result
	items=tf_idf_key.items()
	#print "ITEMS"
	#print items
	items.sort(key=itemgetter(1),reverse=True)
	f=open(result,"w")
	maxx=items[0][1]
	#print "MAXX=",maxx
	for i,t in items:
		t=float(t)/float(maxx)
		#if len(i.split())!=1:
		i=stem_token_function(stemmer_name,i.strip())
		f.write(str(i)+"::"+str(t)+"\n")
	f.close()
	os.system('chmod 777 '+result)

def getfreqkeys(key_grams,tokens):
	for g in key_grams:
		key_grams_count[g]=tokens.count(g)


def gettfidf_keys():
	for t in key_grams_count.keys():
		t=t.lower()
		res=0
		for dd in document:
			if t in dd.grams.keys():
				res=res+1
		try:
			idf_key[t]=float(doc_count)/(float(1)+float(res))
			tf_idf_key[t]=float(key_grams_count[t])*float(idf_key[t])
		except:
			nothing=0
		
if key_file!="":
	global key_grams_count
	key_grams_count={}
	global idf_key
	idf_key={}
	global tf_idf_key
	tf_idf_key={}
	f=open(key_file,"r")
	data=f.readlines()
	f.close()
	key_grams=[]
	for r in data:
		if r not in key_grams and len(r)>2:
			#r=stem_token(r.rstrip("\n"))
			#key_grams.append(r)
			key_grams.append(r.strip())
	doc_name=(grams_folder+"/"+video_file).split(".")[0]
	result=doc_name+"_key"+ext
	f=open(transcript_folder+"/"+video_file,"r")
	tokens=f.read()
	tarray=tokens.split()
	size=len(tarray)
	getfreqkeys(key_grams,tokens)
	gettfidf_keys()
	write_tfidf_keys(result)

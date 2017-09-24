import sys
from cuewords import cue_words
from stop_words import stopword
import os
import math
global front_rear_stopwords
from operator import itemgetter
from nltk import stem
from stem import *

global file_name
global input_folder
global output_folder
global transcript_location
global untagged_file_ext

front_rear_stopwords=['of','a','an','the','and','or']

def stem_token(stemmer_name,cue_words):
	if stemmer_name=="Porter-Stemmer":
		#print ("Performing Porter Stemming")
		stemmer = stem.PorterStemmer()
		for count in range(len(cue_words)):
			cue_words[count]=stemmer.stem(cue_words[count])
	elif stemmer_name=="Lancaster-Stemmer":
		#print ("Performing Lancaster Stemming")
		stemmer = stem.LancasterStemmer()
		for count in range(len(cue_words)):
			cue_words[count]=stemmer.stem(cue_words[count])
	elif stemmer_name=="WordNet-Lemmatizer":
		#print ("Performing Wordnet Lemmatization")
		stemmer = stem.WordNetLemmatizer()
		for count in range(len(cue_words)):
			cue_words[count]=stemmer.lemmatize(cue_words[count])
	return(cue_words)


class cue:
	def __init__(self,file_name,input_folder,output_folder,max_gram,result_ext,ext):
		self.doc_name=input_folder+"/"+file_name
		#print self.doc_name
		self.input_folder=input_folder
		self.output_folder=output_folder
		#self.count_in_file=transcript_location+"/"+file_name
		self.result=output_folder+"/"+file_name.split("_")[0]+ext
		self.key_result=output_folder+"/"+file_name.split("_")[0]+"_key"+ext
		#print self.result
		self.max_gram=max_gram
		self.extraction_range=5
		self.cuekey=[]
		self.cue_freq={}
		self.sentence=[]
		self.key_freq={}
	def find_defined_words(self):
		global ff
		#print "\n",self.doc_name
		#ff.write("\n\n"+self.doc_name+"\n")
		f=open(self.doc_name,"r")
		data=f.read()
		count=0
		tokens=data.split()
		for k in range(len(tokens)-self.max_gram):
			word=""
			for i in range(self.max_gram):
				word+=tokens[k+i]
				if word in cue_words:
					if word+" "+tokens[k+i+1] in cue_words:
						word=word+" "
						continue
					else:
						start=k+i+1; #print "Cueword",  word
						sentence=""
						sentence1=""
						try:
							for count in range(self.extraction_range):
								sentence1=sentence1+tokens[start+count]+" "
							sentence1=sentence1.rstrip(" ")
								
							#sentence=tokens[start]+" "+tokens[start+1]+" "+tokens[start+2]+" "+tokens[start+3]+" "+tokens[start+4]						
							#sentence1=tokens[start]+" "+tokens[start+1]+" "+tokens[start+2]+" "+tokens[start+3]+" "+tokens[start+4]+" "+tokens[start+5]
						except:
							#sentence=""
							sentence1=""							
						#print "sentence=",word+" "+sentence1
						#ff.write(word+"  "+sentence1+"\n")
						self.find_grams(sentence1)
				else:
					word+=" "
		self.find_freq_cueword()

	def find_freq_cueword(self):
		f=open(self.doc_name,"r")
		stemmed_content=f.read()
		#total_doc=len(doc_cue)
		#print total_doc
		for c in self.cuekey:
                    self.cue_freq[c]=1
            #self.cue_freq[c]=stemmed_content.count(c); print self.cue_freq


	def find_key_freq(self,key_grams):
		f=open(self.doc_name,"r")
		stemmed_content=f.read()
		f.close()
		for g in key_grams:
			self.key_freq[g]=stemmed_content.count(g)

	
	def find_grams(self,sentence):	
		token_array=[]; #print "sentence", sentence
		token_array=sentence.split()
		word=""
		for t in token_array:
			if t not in stopword:
				word+=t+" "
			else:
				break
		word=word.rstrip(" ")

		if word!="" and len(word.split())>1:
			word=self.remove_front_rear_stop_words(word)

		if word!="" and word not in self.cuekey and word not in front_rear_stopwords:
			(self.cuekey).append(word)
			
		return

	def remove_front_rear_stop_words(self,phrase):
		phrase=self.remove_front_stop_word(phrase)
		phrase=self.remove_rear_stop_word(phrase)
		return phrase

	def remove_rear_stop_word(self,phrase):
		token_array=[]
		token_array=phrase.split()
		word=""; print phrase
		for i in range(len(token_array)-1,0,-1):
			if token_array[i] in front_rear_stopwords:
				continue
			else:
				for j in range(i+1):
					word+=token_array[j]+" "
				break
		word=word.rstrip(" "); print word
		return word

	def remove_front_stop_word(self,phrase):
		token_array=[]
		token_array=phrase.split()
		word=""; print phrase
		for i in range(len(token_array)):
			if token_array[i] in front_rear_stopwords:
				continue
			else:
				for j in range(i,len(token_array)):
					word+=token_array[j]+" "
				break;	
		word=word.rstrip(" "); print word
		return word
		

	def display(self):
		f=open(self.result,"w")
		items=self.cue_freq.items()
		#items=self.tfidf.items()
		items.sort(key=itemgetter(1),reverse=True)
		maxx=items[0][1]
		name=self.doc_name.split("/")[1]
		name=name.split(".")[0]+".ckey"
		#name="result/"+name
		#f=open(name,"w")
		for i,t in items:
			f.write(str(i)+"::"+str(t)+"\n")
		f.close()

	def display_key(self):
		f=open(self.key_result,"w")
		items=self.key_freq.items()
		#items=self.tfidf.items()
		items.sort(key=itemgetter(1),reverse=True)
		maxx=items[0][1]
		for i,t in items:
			t=float(t)/float(maxx)
			f.write(str(i)+"::"+str(t)+"\n")
		f.close()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

try:
	#untagged_file_ext=sys.argv[7]
	untagged_file_ext="_untagged.txt"
	file_name=(sys.argv[1]).split(".")[0]+untagged_file_ext
	#print file_name
	#input_folder=sys.argv[2]
	input_folder="output"
	#print input_folder
	#lecture=explode(".",file_name)
	#print complete_file_name
	#output_folder=sys.argv[3]
	output_folder="output"
	#print output_folder	
	stemmer_name=sys.argv[2]
	#print stemmer_name
	max_gram=int(sys.argv[3])
	#print max_gram
	#result_ext=sys.argv[6]
	result_ext="_cue.txt"
	#ext=sys.argv[8]
	ext="_cue.txt"
	#stemmer_name=sys.argv[9]
	key_file=""
	"""if len(sys.argv)-1>9:
		key_file=sys.argv[10]
	else:
		key_file="" """
	
except:	
	print "Arguments Insufficient"
	sys.exit()
	
cue_words=stem_token(stemmer_name,cue_words)
stopword=stem_token(stemmer_name,stopword)
global doc_cue
doc_cue=cue(file_name,input_folder,output_folder,max_gram,result_ext,ext)
#ff=open("cue_keyphrase.txt","w")
doc_cue.find_defined_words()
doc_cue.display()
#ff.close()
if key_file!="":
	f=open(key_file,"r")
	data=f.readlines()
	f.close()
	key_grams=[]
	for r in data:
		if r not in key_grams and len(r)>2:
			r=stem_token_function(stemmer_name,r.rstrip("\n"))
			key_grams.append(r)
			#key_grams.append(r.rstrip("\n"))
	doc_cue.find_key_freq(key_grams)
	doc_cue.display_key()

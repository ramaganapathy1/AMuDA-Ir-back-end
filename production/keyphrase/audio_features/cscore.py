import sys
import math
from operator import itemgetter
from stem import *

global file_name
global input_folder
global output_folder

#print "Argument"+str(len(sys.argv)-1)

try:
	file_name=sys.argv[1]
	#print file_name
	#input_folder=sys.argv[2]
	input_folder="production/keyphrase/output"
	#print input_folder
	#output_folder=sys.argv[3]
	output_folder="production/keyphrase/output"
	#print output_folder
	#result_ext=sys.argv[4]
	result_ext="_cscore.txt"
	#print result_ext
	#grams_ext=sys.argv[5]
	grams_ext="_grams.txt"
	#untagged_file_ext=sys.argv[6]
	untagged_file_ext="_untagged.txt"
	#ext=sys.argv[7]
	ext="_cscore.txt"
	stemmer_name=sys.argv[2]
	key_file=""
	#if (len(sys.argv)-1)>8:
	#	key_file=sys.argv[9]
	#else:
	#	key_file=""
except:
	print "Mandatory Parameters unavailable"
	sys.exit()

class cscore:
	def __init__(self,name,grams,result):
		self.doc_name=name
		#print name
		self.grams=grams
		self.freq={}
		self.cscore_gram={}
		self.result=result
		self.max_gram_length=0
		for g in self.grams:
			l=len(g.split())
			if l>self.max_gram_length:
				self.max_gram_length=l
	def find_cscore(self):
		f=open(self.doc_name,"r")
		#print self.doc_name
		data=f.read()
		for g in self.grams:
			high_grams=[]
			len_g=len(g.split())
			#print "len_g :",len__g
			#print "self.max_gram_length:",self.max_gram_length
			self.freq[g]=data.count(g)
			#print g,self.freq[g]
			if len_g==0:
				continue
			#if len_g==2:
			#	print "testing here"
			if len_g==self.max_gram_length:
				self.cscore_gram[g]=math.log(len_g,2)*self.freq[g]
				#print "self.cscore_gram[g]:",self.cscore_gram[g]
			else:
				for h in self.grams:
					if h!=g and len(h.split())>len_g and found_string(g,h)==True:
							if h not in high_grams:
								high_grams.append(h)
				if len(high_grams)>0:
					high_grams_freq=0
					for h in high_grams:
						try:
							high_grams_freq+=self.freq[h]
						except:
							high_grams_freq+=0
					self.cscore_gram[g]=math.log(len_g,2)*(self.freq[g]-(high_grams_freq/len(high_grams)))
				else:
					self.cscore_gram[g]=math.log(len_g,2)*self.freq[g]
						
	def display(self):
		#print "RESULT",self.result
		f=open(self.result,"w")
		items=self.cscore_gram.items()
		#print "items:",items
		items.sort(key=itemgetter(1),reverse=True)
		maxx=items[0][1]
		for i,t in items:
			f.write(str(i)+"::"+str(t)+"\n")
		f.close()

def found_string(str1, str2):
    return ' ' + str1 + ' ' in ' ' + str2 + ' '			

name=(file_name).split(".")[0]
f_name=input_folder+"/"+name+grams_ext
transcript_name=input_folder+"/"+name+untagged_file_ext
result=output_folder+"/"+name+ext
print f_name
f=open(f_name,"r")
data=f.readlines()
f.close()
grams=[]
for r in data:
	grams.append(r.rstrip("\n"))
g=cscore(transcript_name,grams,result)
g.find_cscore()
g.display()

if key_file!="":
	f=open(key_file,"r")
	data=f.readlines()
	f.close()
	key_grams=[]
	for r in data:
		if r not in key_grams and len(r)>2:
			r=stem_token_function(stemmer_name,r.rstrip("\n"))
			key_grams.append(r)
	result=output_folder+"/"+name+"_key"+ext
	h=cscore(transcript_name,key_grams,result)
	h.find_cscore()
	h.display()

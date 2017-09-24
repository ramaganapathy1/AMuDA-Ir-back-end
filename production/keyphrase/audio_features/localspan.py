import sys
import re
import numpy
import math
from operator import itemgetter
from nltk import stem
from stem import *

class localspan:

	def __init__(self,name,input_folder,output_folder,grams,result_ext,untagged_file_ext,ext):
		self.result=output_folder+"/"+name+ext
		self.doc_name=input_folder+"/"+name+untagged_file_ext
		self.grams=grams
		#print self.grams
		self.local_span={}
		f=open(self.doc_name,"r")
		self.dtokens=f.read().lower()
		f.close()
		self.tkn=self.dtokens.split()
		#print self.dtokens
		self.disp={}
		self.segment_count=5
		self.size=len(self.tkn)
		self.segment=self.size/self.segment_count

	def find_dispersion(self):
		global max_gram
		for text_search1 in self.grams:
			text_search1=text_search1.lower()
			#print text_search1
			#gap=[]
			l=len(text_search1.split())
			if l>1:
				total_count=(self.dtokens).count(text_search1)
				avg_count=float(total_count)/float(self.segment)
				#print text_search1,total_count
				if total_count>2:
					seg_count=[]
					for i in range(self.segment_count):
						gp=[]
						start=i*self.segment
						end=start+self.segment
						array=self.tkn[start:end]
						start1=(i*self.segment)+(self.segment/2)
						end1=start+self.segment
						if end1>self.size:
							array1=self.tkn[start1:self.size]
						else:
							array1=self.tkn[start1:end1]

						data=""
						for a in array:
							data+=a+" "
						seg_count.append(abs(data.count(text_search1)-avg_count))
						for a in array1:
							data+=a+" "
						seg_count.append(abs(data.count(text_search1)-avg_count))
					#print text_search1,seg_count
					#if total_count>2:
					s=max(seg_count)
					#span=(float(s))*math.log(total_count,2)
					span=(float(s))
					self.local_span[text_search1]=span
									


	def display(self):
		items=self.local_span.items()
		#print items
		items.sort(key=itemgetter(1),reverse=True)
		#print items
		span_max=items[0][1]
		f=open(self.result,"w")
		for i,t in items:
			f.write(i+"::"+str(t)+"\n")
		f.close()


global file_name
global input_folder
global output_folder

try:
	file_name=sys.argv[1]
	#input_folder=sys.argv[2]
	input_folder="output"
	#output_folder=sys.argv[3]
	output_folder="output"
	max_gram=sys.argv[2]
	#result_ext=sys.argv[5]
	result_ext="_localspan.txt"
	#gram_ext=sys.argv[6]
	gram_ext="_grams.txt"
	#untagged_file_ext=sys.argv[7]
	untagged_file_ext="_untagged.txt"
	ext="_localspan.txt"
	stemmer_name=sys.argv[3]
	key_file=""

except:
	print "Mandatory Parameters unavailable"
	sys.exit()

name=(file_name).split(".")[0]
f_name=input_folder+"/"+name+gram_ext
f=open(f_name,"r")
data=f.readlines()
f.close()
grams=[]
for r in data:
	grams.append(r.rstrip("\n"))
#print grams
doc_disp=localspan(name,input_folder,output_folder,grams,result_ext,untagged_file_ext,ext)		

doc_disp.find_dispersion()
doc_disp.display()
#	doc_count+=1
#print "\n"

#print "DONE................"
if key_file!="":
	f=open(key_file,"r")
	data=f.readlines()
	f.close()
	grams=[]
	for r in data:
		if r not in grams and len(r)>2:
			r=stem_token_function(stemmer_name,r.rstrip("\n"))
			grams.append(r)
			#grams.append(r.strip())
	doc_key_disp=localspan(name,input_folder,output_folder,grams,result_ext,untagged_file_ext,"_key"+ext)
	doc_key_disp.find_dispersion()
	doc_key_disp.display()

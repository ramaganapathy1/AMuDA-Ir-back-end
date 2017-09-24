import sys
import os
from stopwords_video import vid_stopwords
import nltk
from nltk import stem

global stemmer_name
global delimiter
global video_folder
global video_name
global stem_to_root
stem_to_root={}

try:
	video_name=sys.argv[1]
	video_name=video_name.split(".txt")[0]
	video_folder="videotextslides"
	input_folder=video_folder+"/"+video_name
	#feature_list=sys.argv[2]
	#feature=feature_list.split(",")
        delimiter='::'
	#max_gram=sys.argv[3]
	output_folder="output"
	stemmer_name=sys.argv[2]
except:
	print "No Mandatory Parameters"
	sys.exit()

if not os.path.exists(input_folder):
	print "Invalid Path"
	sys.exit()

class video_features:
	input_data=["row_num","text_height","text"]
	total_input=3
	def __init__(self,file_name,content,output_folder):

		self.file_name=file_name
		#print self.file_name
		self.content=content
		#print "CONTENT:",self.content
		#print "*****************************************************************"
		#Initializing input_data
		self.row_num=[]
		self.text_height=[]
		self.text=[]
		self.stem_text=[]
		
		#Initializing feature variables
		self.textsize=[]
		self.cont_occurance_ratio={}
		self.frequency_ratio={}
		self.heading={}

		for line in self.content:
			data=line.split(delimiter)
			if len(data)==video_features.total_input:
				self.row_num.append(int(data[0].split(" ")[1]))              
                       		self.text_height.append(int(data[1].split(" ")[1]))
                        	self.text.append(data[2].rstrip("\n").lower())
		#print self.text
		#print "*****************************************************************"
		self.res_folder=output_folder+"/"+video_name
		#self.res_folder=video_folder+"_stem"
		self.result=self.res_folder+"/"+self.file_name
		#print "RESULT:"+self.result
		#self.root_file=self.res_folder+"/"+self.
		
	def stem_text_contents(self):
		if stemmer_name=="Porter-Stemmer":
			stemmer = stem.PorterStemmer()
			for counter in range(len(self.text)):
				text_tokens=self.text[counter].split()
				stem_text=""
				for t in text_tokens:
					root_word=t
					stem_text=stem_text+stemmer.stem(t)+" "
					stem_to_root[stemmer.stem(t)]=root_word
				stem_text=stem_text.strip(" ")
				self.stem_text.append(stem_text)
		elif stemmer_name=="Lancaster-Stemmer":
			stemmer = stem.LancasterStemmer()
			for counter in range(len(self.text)):
				text_tokens=self.text[counter].split()
				stem_text=""
				for t in text_tokens:
					root_word=t
					stem_text=stem_text+stemmer.stem(t)+" "
					stem_to_root[stemmer.stem(t)]=root_word
				stem_text=stem_text.strip(" ")
				self.stem_text.append(stem_text)
		elif stemmer_name=="WordNet-Lemmatizer":
			stemmer = WordNetLemmatizer()
			for counter in range(len(self.text)):
				text_tokens=self.text[counter].split()
				stem_text=""
				for t in text_tokens:
					root_word=t
					stem_text=stem_text+stemmer.lemmatize(t)+" "
					stem_to_root[stemmer.stem(t)]=root_word
				stem_text=stem_text.strip(" ")
				self.stem_text.append(stem_text)
		else:
				self.stem_text=self.text
	def write_to_file(self):
		if not os.path.exists(self.res_folder):
			os.makedirs(self.res_folder)
		fres=open(self.result,"w")
		#print self.result
		for t in range(len(self.stem_text)):
			data="Row "+str(self.row_num[t])+delimiter+"Height "+str(self.text_height[t])+delimiter+str(self.stem_text[t])+"\s**s/"+str(self.text[t])+"\n"
			fres.write(data)
		fres.close()

def stem_to_root_file(root_file):
	rhandle=open(root_file,"w")
	for r in stem_to_root.keys():
		rhandle.write(r+"::"+stem_to_root[r]+"\n")
	rhandle.close()
			
	
files_in_folder=os.listdir(input_folder)
txt_files=[]
for f in files_in_folder:
	if f.endswith(".txt"):
		txt_files.append(f)

video_object=[]
object_count=0
for f in sorted(txt_files):
	content=[]
	ftxt=open(input_folder+"/"+f,"r")
	content=ftxt.readlines()
        ftxt.close()
	video_object.append(video_features(f,content,output_folder))
	video_object[object_count].stem_text_contents()
	video_object[object_count].write_to_file()
	object_count=object_count+1

root_file=output_folder+"/"+video_name+"_vroot.txt"
stem_to_root_file(root_file)

import sys
import os
from nltk import stem



try:
	tab_files=sys.argv[1]
        print tab_files
	output_file=sys.argv[2]
        print output_file
	input_folder=sys.argv[3]
        print input_folder
	keys_folder=sys.argv[4]
        print keys_folder
	output_folder=sys.argv[5]
        print output_folder
	stemmer_name=sys.argv[6]
        print stemmer_name

except:
	print "No Mangatory Parameters"
	sys.exit()


class Ddict(dict):
    def __init__(self, default=None):
        self.default = default

    def __getitem__(self, key):
        if not self.has_key(key):
            self[key] = self.default()
        return dict.__getitem__(self, key)

def stem_words(keywords,stemmer_name):
	if stemmer_name=="Porter-Stemmer":
		stemmer = stem.PorterStemmer()
		for k in range(len(keywords)):
			word_token=keywords[k].split(" ")
			word=""
			for w in word_token:
				w=stemmer.stem(w)
				word=word+w+" "
			word=word.rstrip(" ")
			keywords[k]=word.lower()
	if stemmer_name=="Lancaster-Stemmer":
		stemmer = stem.PorterStemmer()
		for k in range(len(keywords)):
			word_token=keywords[k].split(" ")
			word=""
			for w in word_token:
				w=stemmer.stem(w)
				word=word+w+" "
			word=word.rstrip(" ")
			keywords[k]=word.lower()
	if stemmer_name=="WordNet-Lemmatizer":
		stemmer = stem.PorterStemmer()
		for k in range(len(keywords)):
			word_token=keywords[k].split(" ")
			word=""
			for w in word_token:
				w=stemmer.stem(w)
				word=word+w+" "
			word=word.rstrip(" ")
			keywords[k]=word.lower()
	return(keywords)

def convert_keys_to_stem(complete_file_path,keys_folder,stemmer_name):	
	file_handle=open(complete_file_path,"r")
	keys_list=file_handle.readlines()
	keywords=[]
	for lines in keys_list:
		keywords.append(lines.strip())
	keywords=stem_words(keywords,stemmer_name)
        print complete_file_path
	#print keywords
	return keywords

def write_to_all_file(input_tab_name,handle_all,keywords,counter,append_file,feature_line):
	file_handle=open(input_tab_name,"r")
	file_data=file_handle.readlines()
	line_number=0
        stemmer = stem.PorterStemmer()
        true_count=0
        token_list=[]
        if (append_file==1 and feature_line!=file_data[0]):
            print "<font color=red><b>Incompatible Feature Data. Please create a new file for this feature profile</b></font>"
        else:
            if (counter==0 and append_file==0):
                for i in range(3):
                    handle_all.write(file_data[i])
        
            for i in range(len(file_data)):
                if i<3:
                    continue
                else:
                    token=file_data[i].split("\t")
                    
                    trainingKeyphrase=token[0].strip()
                    trainingKeyphrase_list=trainingKeyphrase.split(" ")
                    word=""
                    for w in trainingKeyphrase_list:
                        w=stemmer.stem(w)
                        word=word+w+" "
                    word=word.rstrip(" ")
                    trainingKeyphrase=word
                    token_list.append(trainingKeyphrase)
                    if trainingKeyphrase in keywords:
                        file_data[i]=file_data[i].replace("False","True")
                    handle_all.write(file_data[i])
    
        for keywordIndex in keywords:
            if keywordIndex in token_list:
                true_count=true_count+1
            else:
                print keywordIndex
        print true_count
        
    #print token_list	

tab_file_list=tab_files.split(",")
print tab_file_list
if os.path.exists(output_folder+"/"+output_file):
	handle=open(output_folder+"/"+output_file,"r")
	content=handle.readlines(); #print content
	feature_line=content[0]
	handle.close()
	handle_all=open(output_folder+"/"+output_file,"a")
	append_file=1
else:
	feature_line=""
	handle_all=open(output_folder+"/"+output_file,"w")
	append_file=0

counter=0
for t in tab_file_list:
	key_file_list=t.split(".")
	key_file=key_file_list[0]
	complete_file_path=keys_folder+"/"+key_file+".key"
        print complete_file_path
	keywords=convert_keys_to_stem(complete_file_path,keys_folder,stemmer_name)
        print "keywords length" 
        print len(keywords)
	input_tab_name=input_folder+"/"+t
	write_to_all_file(input_tab_name,handle_all,keywords,counter,append_file,feature_line)
	counter=counter+1
	#print input_tab_name
	#os.system("rm "+input_tab_name)


handle_all.close()

import sys
import os
from nltk import stem
from stem import *

try:
	file_name=sys.argv[1]
	file_name=file_name.split(".txt")[0]
	print file_name
	feature_list=sys.argv[2]
	print feature_list
	#feature_file_path=sys.argv[3]
	feature_file_path="production/keyphrase/output"
	#grams_folder=sys.argv[4]
	grams_folder="production/keyphrase/output"
	#gram_ext=sys.argv[5]
	gram_ext="_grams.txt"
	#vgram_ext=sys.argv[6]
	vgram_ext="_vgramsroot.txt"
	extension_list=sys.argv[3]
	print extension_list
	extension_list=extension_list.strip("'")
	extension_list=extension_list.strip(",")
	#print extension_list
	stemmer_name=sys.argv[4]
	print stemmer_name
	#print stemmer_name
	audio_root_file=file_name+"_root.txt"
	video_root_file=file_name+"_vroot.txt"
	stem_to_root={}
	file_type=""
	key_file=""

	"""if (len(sys.argv)-1)>8:
		file_type=sys.argv[9]
		key_file=sys.argv[10]
	else:
		file_type=""
		key_file="" """

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

def write_to_file(file_name,feature_list,feature_file_path,grams_folder,gram_ext,vgram_ext,stem_to_root,file_type,key_file,extension_list):
    print "EXT",extension_list
    
    if file_type=="":
        output_file=feature_file_path+"/"+file_name+".tab"
        grams_file=grams_folder+"/"+file_name+gram_ext ; grams=[]
        try:
            fgrams=open(grams_file,"r")
            grams_list=fgrams.readlines()
            
            fgrams.close()
            for g in grams_list:
                grams.append(g.rstrip("\n"))


        except:
            nothing = 0

        grams_file=grams_folder+"/"+file_name+vgram_ext
        try:
            fgrams=open(grams_file,"r")
            grams_list=fgrams.readlines()
            fgrams.close()
            for g in grams_list:
                grams.append(g.rstrip("\n"))

        except:
            nothing=0
    else:
        output_file=feature_file_path+"/"+file_name+"_key.txt"
        fgrams=open(key_file,"r")
        grams_list=fgrams.readlines()
        fgrams.close()
        grams=[]
        for g in grams_list:
            if len(g)>2:
                g=stem_token_function(stemmer_name,g.strip())
                grams.append(g)
            #grams.append(g.strip())

   
    features=feature_list.split(",")
    extensions=extension_list.split(",")
    features_values=Ddict( dict ) ;stemmed_grams=[]
    #for f in features:
    counter=0
    for f in extensions:
        #feature_file=feature_file_path+"/"+file_name+"_"+f+".txt"
        feature_file=feature_file_path+"/"+file_name+f
        print feature_file
        ff=open(feature_file,"r")
        data=ff.readlines()
        ff.close()
        if len(data)==0:
            features_values[features[counter]][""]=0
        #os.system("rm "+feature_file)
        for line in data:
            line=line.rstrip("\n")
            content=line.split("::")
            features_values[features[counter]][content[0]]=content[1]
        counter=counter+1
    f=open(output_file,"w")
    f.write("keyphrase\t")
    #print features_values
    for key in features_values.keys():
        f.write(key+"\t")
    if file_type=="":
        f.write("keyword\n")
        f.write("d\t")
        for key in features_values.keys():
            f.write("c\t")
        f.write("d\n")
        f.write("m\t")
        for key in features_values.keys():
            f.write("\t")
        f.write("class\n")
    else:
        f.write("\n");

    for g in grams:
        word_list=g.split("::")
        if word_list[0] not in stemmed_grams:
                stemmed_grams.append(word_list[0])
                f.write(word_list[0]+"\t")
                for key in features_values.keys():
                    if word_list[0] in features_values[key].keys():
                        f.write(features_values[key][word_list[0]]+"\t")
                    else:
                        f.write("0.0\t")
                if file_type=="":
                    f.write("False\n")
                else:
                    f.write("\n")	
    f.close()
    os.system("chmod 777 "+output_file);

if os.path.exists(grams_folder+"/"+audio_root_file):
	handler=open(grams_folder+"/"+audio_root_file,"r")
	contents=handler.readlines()
	handler.close()
	for line in contents:
		line_list=line.split("::")
		stem=line_list[0].strip()
		root=line_list[1].strip()
		stem_to_root[stem]=root
if os.path.exists(grams_folder+"/"+video_root_file):
	handler=open(grams_folder+"/"+video_root_file,"r")
	contents=handler.readlines()
	handler.close()
	for line in contents:
		line_list=line.split("::")
		stem=line_list[0].strip()
		root=line_list[1].strip()
		stem_to_root[stem]=root
		

write_to_file(file_name,feature_list,feature_file_path,grams_folder,gram_ext,vgram_ext,stem_to_root,file_type,key_file,extension_list)

files=os.listdir(feature_file_path)
"""for f in files:
	if (f.startswith(file_name) and f!=file_name+".tab"):
		os.system("rm "+feature_file_path+"/"+f)"""
		

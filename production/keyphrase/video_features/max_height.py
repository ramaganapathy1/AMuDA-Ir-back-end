import os
import sys
import math
from operator import itemgetter

def remove_hyphen(g):
    if g.count("-")>0:
        temp=g.split("-")
        l=len(temp)
        word=""
        for i in range(l):
            word+=temp[i]+" "
        g=word.rstrip(" ")
    return g

def remove_special_case(g):
    token=g.split()
    word=""
    for t in token:
        t=t.rstrip(" ")
        t=t.lstrip(" ")
        t=t.rstrip("()")
        t=t.lstrip("()")
        t=t.lstrip("(")
        t=t.rstrip("(")
        t=t.rstrip(")")
        t=t.lstrip(")")
        t=t.lstrip("[")
        t=t.rstrip("]")
        t=t.lstrip("{")
        t=t.rstrip("}")
        t=t.rstrip(":")
        t=t.lstrip(":")
        t=t.lstrip(",")
        t=t.rstrip(",")
        t=t.rstrip(".")
        word+=t+" "
    word=word.rstrip(" ")
    #print word
    return word

try:
    input_grams=sys.argv[1].split(".txt")[0]+"_vgrams.txt";
    #print input_grams
    input_data_folder=sys.argv[2]
    output_folder=sys.argv[3]
    ext=sys.argv[4]
    key_file=""
    #if (len(sys.argv)-1)>4:
    #		key_file=sys.argv[5]
    #else:

except:
	print "No Mandatory Parameters"	
	sys.exit()

class max_height:
    def __init__(self,input_grams,input_data_folder,output_folder,ext,key,key_file):
        self.input_grams=input_grams
        #print self.input_grams
        self.input_data_folder=input_data_folder
        self.output_folder=output_folder
        self.phrase=[]
        self.input_files=[]
        self.stemTextFolder=self.input_grams.rstrip("_vgrams.txt")
        #print self.stemTextFolder
        if self.stemTextFolder=="embsy":
            self.stemTextFolder=self.stemTextFolder+"s"
        #print self.stemTextFolder
        if key=="no":
            #print self.input_data_folder+"/"+self.input_grams
            f=open(self.input_data_folder+"/"+self.input_grams,"r")
        else:
            f=open(key_file,"r")

        phrase=f.readlines()
        f.close()

        for p in phrase:
            (self.phrase).append(p.rstrip("\n"))

        #print self.phrase; 
        self.max_height={}
        #print self.stemTextFolder
        #print self.input_data_folder+"/"+self.stemTextFolder
        self.total_slides=len(os.listdir(self.input_data_folder+"/"+self.stemTextFolder))
        #size=len(input_data_folder_split)
        self.res_file=self.stemTextFolder
        if key=="no":
            self.height_files=self.output_folder+"/"+self.res_file+ext
        else:
            self.height_files=self.output_folder+"/"+self.res_file+"_key"+ext

    def find_max_height(self):
        if not os.path.isdir(self.input_data_folder+"/"+self.stemTextFolder):
            print "Input folder does not exist"
            sys.exit()
        else:
            self.input_files=os.listdir(self.input_data_folder+"/"+self.stemTextFolder)
            for p in self.phrase:
                self.max_height[p]=1
                for txt_files in sorted(self.input_files):
                    if txt_files.endswith(".txt"):
                        file_handle=open(self.input_data_folder+"/"+self.stemTextFolder+"/"+txt_files,"r")
                        data=file_handle.readlines()
                        for line in data:
                            stemmedPart=line.rstrip("\n").split("::")[2]
                            stemmedPart=stemmedPart.split("\s**s/")[0]
                            stemmedPart=remove_hyphen(stemmedPart)
                            stemmedPart=remove_special_case(stemmedPart)
                            #print line.rstrip("\n")
                            #print p
                            #print stemmedPart
                            if p in line:
                                #print line,p
                                line_split=line.split("::")
                                for l in line_split:
                                    #print l
                                    if "Height" in l:
                                        cur_height=int(l.split()[1])
                                        if cur_height>self.max_height[p]:
                                            self.max_height[p]=cur_height
                        file_handle.close()
                #print p,self.max_height[p]


    def write_to_file(self):
        items=(self.max_height).items()
        items.sort(key=itemgetter(1),reverse=True)
        f=open(self.height_files,"w")
        for i,t in items:
            f.write(str(i)+"::"+str(t)+"\n")
        f.close()
        
        
feature_object=max_height(input_grams,input_data_folder,output_folder,ext,'no',key_file)
feature_object.find_max_height()
feature_object.write_to_file()

if key_file!="":
	feature_object=max_height(input_grams,input_data_folder,output_folder,ext,'yes',key_file)
	feature_object.find_max_height()
	feature_object.write_to_file()
	

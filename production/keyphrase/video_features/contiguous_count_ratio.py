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
    input_grams=sys.argv[1].split(".txt")[0]+"_vgrams.txt"
    print input_grams
    input_data_folder="output"
    output_folder="output"
    ext_name=sys.argv[2]
    key_file=""
    """if (len(sys.argv)-1)>4:
        key_file=sys.argv[5]
    else:
        key_file="" """
except:
	print "No Mandatory Parameters"	
	sys.exit()

class contiguous_count_ratio:
    def __init__(self,input_grams,input_data_folder,output_folder,key,key_file):
        self.input_grams=input_grams; 
        self.input_data_folder=input_data_folder; self.slideFolder=self.input_data_folder+"/"+self.input_grams.rstrip("_vgrams.txt"); print self.slideFolder
        self.output_folder=output_folder
        self.phrase=[]
        self.input_files=[]; print self.input_data_folder+"/"+self.input_grams
        if key=="no":
            f=open(self.input_data_folder+"/"+self.input_grams,"r")
        else:
            f=open(key_file,"r")

        phrase=f.readlines()
        f.close()
        for p in phrase:
            if len(p)>2:
                (self.phrase).append(p.rstrip("\n")); 
            else:
                print p
                
        self.contiguous_count={}
        self.contiguous_count_ratio={}
        self.frequency_ratio={}
        self.total_slides=len(os.listdir( self.slideFolder)); print self.total_slides
        #input_data_folder_split=self.input_data_folder.split("/")
        #size=len(input_data_folder_split)
        #self.res_file=input_data_folder_split[size-1]
        self.res_file=self.input_grams.split("_")[0]
        if key=="no":
            self.cont_files=self.output_folder+"/"+self.res_file+"_cont.txt"
        else:
            self.cont_files=self.output_folder+"/"+self.res_file+"_key_cont.txt"

    def find_contiguous_count(self):
        if not os.path.isdir(self.slideFolder):
            print "Input folder does not exist"
            sys.exit()
        else:
            self.input_files=os.listdir(self.slideFolder)
            for p in self.phrase:
                #print p
                phrase_array=[]
                self.contiguous_count[p]=[]
                counter=0
                prev_counter=0
                for txt_files in sorted(self.input_files):
                    if txt_files.endswith(".txt"):
                        data=""
                        file_handle=open(self.slideFolder+"/"+txt_files,"r")
                        datalines=file_handle.readlines()                            
                        file_handle.close()
                        for d in datalines:
                            stemmedPart=d.rstrip("\n").split("::")[2]
                            stemmedPart=stemmedPart.split("\s**s/")[0]
                            stemmedPart=remove_hyphen(stemmedPart)
                            stemmedPart=remove_special_case(stemmedPart)
                            data=data+" "+stemmedPart
                        #print data
                        data_count=data.count(p)
                        #print data_count
                        if (data_count>0):	
                            #print p,data_count,counter,txt_files
                            try:
                                phrase_array[counter]=phrase_array[counter]+data_count
                            except:
                                phrase_array.append(data_count)
                            #print phrase_array
                            prev_counter=counter
                        else:
                            if counter==prev_counter and len(phrase_array)>0:
                                counter=prev_counter+1

                #print p,phrase_array
                self.contiguous_count[p]=phrase_array
                #print p,self.contiguous_count[p]

    def find_contiguous_count_ratio(self):
        for p in self.phrase:
            try:
                self.contiguous_count_ratio[p]=float(max(self.contiguous_count[p]))/float(self.total_slides)
                self.contiguous_count_ratio[p]=self.contiguous_count_ratio[p]*math.log(sum(self.contiguous_count[p]),2)
            except:
                self.contiguous_count_ratio[p]=0
            #print p,self.contiguous_count[p],self.contiguous_count_ratio[p]

    def write_to_file(self):
        items=(self.contiguous_count_ratio).items()
        items.sort(key=itemgetter(1),reverse=True)
        f=open(self.cont_files,"w")
        for i,t in items:
            f.write(str(i)+"::"+str(t)+"\n")
        f.close()

feature_object=contiguous_count_ratio(input_grams,input_data_folder,output_folder,'no',key_file)
feature_object.find_contiguous_count()
feature_object.find_contiguous_count_ratio()
feature_object.write_to_file()

if key_file!="":
	feature_object=contiguous_count_ratio(input_grams,input_data_folder,output_folder,'yes',key_file)
	feature_object.find_contiguous_count()
	feature_object.find_contiguous_count_ratio()
	feature_object.write_to_file()

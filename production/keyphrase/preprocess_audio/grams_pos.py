#Sample Command: python grams_pos.py ds8.txt "/var/www/metadata/output/preprocess_audio" "/var/www/metadata/output/preprocess_audio" 4 pos_filter.txt
import sys
from stop_words import stopword
import os
from nltk import stem
class gram:
    def __init__(self,file_name,input_folder,output_folder,complete_file_name,max_gram,pos_filter_file,gram_ext):
        self.doc_name=complete_file_name
        #print self.doc_name
        self.grams={}
        f=open(self.doc_name,"r")
        self.max_gram=max_gram
        self.pos_filter_file=pos_filter_file
        self.tokens=f.read()
        #print self.tokens
        self.tarray=self.tokens.split()
        #print self.tarray
        self.size=len(self.tarray)
        #self.result_file=file_name.split(".")[0]+".grams"
        self.result=output_folder+"/"+file_name.split("_")[0]+gram_ext
        print "self.result" + self.result
        self.pos_filter={}
        #(self.doc_name).split("/")[1]
        #self.result="result/"+self.result.split(".")[0]+".grams"
        #self.one_g="result/"+self.result.split(".")[0]+".onegrams"
        self.final_grams=[];    self.final_unstemmed_grams=[]

    def extract_gram(self,n):
        for i in range(len(self.tarray)-n):
            flag=0; d_unstemmed=""
            d=""  
            unstemmedToken=[]
            token=[]
            tag=[]
            for j in range(n):
                token.append(self.tarray[i+j].split("/")[0])
                tag.append(self.tarray[i+j].split("/")[1])
                unstemmedToken.append(self.tarray[i+j].split("/")[2])
                if (not is_number(token[j]) and token[j]!=" " and token[j]!=""):
                    d=d+token[j]+" "
                    d_unstemmed=d_unstemmed+ unstemmedToken[j].rstrip(".")+" "           
                else :
                    flag=1
                    break
            d=d.rstrip(" ")
            d_unstemmed=d_unstemmed.rstrip(" ")
#            if d_unstemmed.startswith("sub netting"):
#                print d_unstemmed
#                print d.split()
            #word=d.split()
            word=d_unstemmed.split()
            l=len(word)
            if (flag==0 and d_unstemmed not in self.final_grams):
                if (word[0].strip() not in stopwordUnstemmed and word[l-1].strip() not in stopwordUnstemmed and len(word[0])>2 and len(word[l-1])>2):
                    if (n in self.pos_filter.keys()):
                        pos_eligible=self.pos_filtering(n,token,tag)
                        if pos_eligible:
                                                    (self.final_grams).append(d_unstemmed.rstrip("."));  
                                                    (self.final_unstemmed_grams).append(d+"::"+d_unstemmed.rstrip(".")); 
                    else:	
                                            (self.final_grams).append(d_unstemmed.rstrip("."));
                                            self.final_unstemmed_grams.append(d+"::"+d_unstemmed.rstrip(".")); 
                        #print "Filter Not Available";
                        #break
    def pos_filtering(self,n,token,tag):
	    #print n
	    #print token
	    #print tag
            for filt in self.pos_filter[n]:
                filt_token=filt.split(",")
                satisfied=0
                for i in range(n):
                    if tag[i].startswith(filt_token[i]) or filt_token[i]=='ANY':	
                        satisfied=1
                    else:
                        satisfied=0
                        break
                if satisfied==1:
                    break
            return(satisfied)
    
    
    def get_pos_filter(self):
	print "posfile :" + pos_filter_file; 
	f_pos=open(self.pos_filter_file,"r")
	pos_content=f_pos.readlines()
        for pos in pos_content:
            pos=pos.rstrip("\n")
            pos=pos.rstrip("\r")
            filter_size=len(pos.split(","))
            #print pos,filter_size
            if filter_size not in self.pos_filter.keys():
                self.pos_filter[filter_size]=[pos,]
            else:
                self.pos_filter[filter_size].append(pos)
	
        #print self.pos_filter

    def write_to_file(self):
        f=open(self.result,"w");count=0
        stemmed_gram_list=[]
        f1=open((self.result).rstrip(".txt")+"root"+".txt", "w")
        for k in (self.final_unstemmed_grams):
            stemmedGram=k.split("::")[0]
            if stemmedGram not in stemmed_gram_list:
                f.write(stemmedGram.replace("'","")+"\n")
                stemmed_gram_list.append(stemmedGram)
            f1.write(k.replace("'", "")+"\n")
        f1.close()
        f.close()
        #os.system('chmod 777 '+self.result)

    
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
            #print word+" repeated"
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
        stemmer = stem.WordNetLemmatizer()
        for count in range(len(stopword)):
            stopword[count]=stemmer.lemmatize(stopword[count])
    return(stopword)

try:
    file_name=sys.argv[1]
    file_name_list=file_name.split(".")
    file_name=file_name_list[0]+"_tagged.txt"
    print "file_name:" + file_name
    #input_folder=sys.argv[2]
    input_folder="output"
    #print input_folder
    complete_file_name=input_folder+"/"+file_name
    #print complete_file_name
    #output_folder=sys.argv[3]
    output_folder="output"
    #print output_folder	
    max_gram=int(sys.argv[2])
    #print max_gram
    pos_filter_file=sys.argv[3]
   # print "pos_filterfile :" + pos_filter_file
    stemmer_name=sys.argv[4]
    gram_ext="_grams.txt"

except:
    print "No argument"
    sys.exit()

stopwordUnstemmed=[]
stopwordUnstemmed.extend(stopword)
stopword=stem_token(stemmer_name,stopword)
#for itr in range(len(stopword)):
#    print stopwordUnstemmed[itr],  stopword[itr]
#print stopword
g=gram(file_name,input_folder,output_folder,complete_file_name,max_gram,pos_filter_file,gram_ext)
g.get_pos_filter()
#print "hello dude"
#g.extract_gram(2)
for i in range(max_gram,0,-1): 
#print i
    g.extract_gram(i)
g.write_to_file()

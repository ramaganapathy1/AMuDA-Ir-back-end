import os
import sys
from stopwords_video import vid_stopwords
from stop_words import stopword
import nltk
import re
from nltk import stem
stemmer = stem.PorterStemmer()
from operator import itemgetter
import math

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

def stop_word_check(t):
    token=t.split()
    token_len=len(token)
    if token[0] not in start_end_stop  and token[token_len-1] not in start_end_stop and token[token_len-1] not in end_stop and token[0] not in stopword and token[token_len-1] not in stopword:
        return 1
    else:
        return 0

def remove_phrase_with_spl_char():
    remove_phrase=[]
    for word in unStem_phrase:
        word_token=word.split("::")
        for chars in symbols+numbers:
            if chars in word_token[0]:
                remove_phrase.append(word_token[0]+"::"+word_token[1])
                break
                
    for word in remove_phrase:
        unStem_phrase.remove(word)


def write_phrase():
    output_file_name=folder_name.split("/")
    size=len(output_file_name)
    res_file=output_folder+"/"+output_file_name[size-1]+ext
    f=open(res_file,"w")
    f1=open(res_file.rstrip(".txt")+"root"+".txt", "w")
    stemmed_gram_list=[]
        
    for p in unStem_phrase:
        stemmedPart=p.split("::")[0]
        if stemmedPart not in stemmed_gram_list:
            f.write(stemmedPart+"\n")
            stemmed_gram_list.append(stemmedPart)
        f1.write(p+"\n")
    f.close()
    f1.close()
    

try:
    folder_name=sys.argv[1]
    folder_name="output/"+folder_name.split(".txt")[0]
    max_gram=sys.argv[2]
    #print max_gram
    output_folder="output"
    ext="_vgrams.txt"
except:
	print "No Mandatory Parameters"
	sys.exit()

global start_end_stop
start_end_stop=['of','in','at','for',"a","an","the"]
global end_stop
end_stop=["a","an","the"]
global symbols
symbols=["+","-","*","/","-","@","?",".","(",")","[","]","{","}", "&", "="]
global video
global numbers
numbers=['1','2','3','4','5','6','7','8','9','0']
video=[]
global max_height
max_height=0
global phrase
phrase=[]
global unStem_phrase
unStem_phrase=[]
#Initially Unique text sides for each video has to be identified and stored inside a folder "X" under input folder


#dir_name="input/ds4"
#res_file="ds4.key"
files=os.listdir(folder_name)
text_files=[]
for f in files:
    if f.endswith(".txt"):
        text_files.append(f)

class video_text:
    def __init__(self,doc_name,height,text,unStemmed_text, slideContents, slideContents_unstemmed):
        self.doc_name=doc_name
        self.height=height
        self.text=text
        self.unStemmed_text=unStemmed_text
        self.cand_phrase={}
        self.ext=ext
        self.slideContents=slideContents
        self.slideContents_unstemmed=slideContents_unstemmed

    def extract_grams(self,token,token_Unstemmed, token_size):
        grams=[]
        gramsUnstemmed=[]
        #print nltk.ngrams(token,token_size)
        grams.extend(nltk.ngrams(token,token_size))
        gramsUnstemmed.extend(nltk.ngrams(token_Unstemmed,token_size))
        #print grams
        for g in range(len(gramsUnstemmed)):
            gramStringFormat=""
            for listcontents in gramsUnstemmed[g]:
                gramStringFormat= gramStringFormat+" "+listcontents
            #print gramStringFormat
            if gramStringFormat not in vid_stopwords and stop_word_check(gramStringFormat):
                word=""
                word_unstemmed=""
                len_g=len(grams[g])
                if gramsUnstemmed[g][0] not in start_end_stop and gramsUnstemmed[g][len_g-1] not in end_stop and gramsUnstemmed[g][len_g-1] not in start_end_stop and gramsUnstemmed[g][0] not in stopword and  gramsUnstemmed[g][len_g-1] not in stopword and len(gramsUnstemmed[g][0])>2 and len(gramsUnstemmed[g][len_g-1])>2:
                    for t in range(len(gramsUnstemmed[g])): 
                        word+=grams[g][t]+" "
                        word_unstemmed+=gramsUnstemmed[g][t]+" "
                    word=word.rstrip(" ")
                    word_unstemmed=word_unstemmed.rstrip(" ")
                    word=remove_special_case(word)
                    word_unstemmed=remove_special_case(word_unstemmed)
                    if word_unstemmed not in (self.cand_phrase).keys(): 
                        self.cand_phrase[word_unstemmed]=1
                        if word_unstemmed not in phrase:
                            phrase.append(word_unstemmed)
                            unStem_phrase.append(word+"::"+word_unstemmed)
                    else:
                        self.cand_phrase[word_unstemmed]+=1
#                    if word not in (self.cand_phrase).keys(): 
#                        self.cand_phrase[word]=1
#                        if word not in phrase:
#                            phrase.append(word)
#                    else:
#                        self.cand_phrase[word]+=1

        if token_size-1>=1:
            self.extract_grams(token,token_Unstemmed, token_size-1)

    def extract_candidate_phrases(self):
        for t in range(len(self.text)):
            #print "self.text[t] ", self.text[t]
            if self.text[t]=="the vector adt":
                print "hi"
            self.text[t]=remove_hyphen(self.text[t])
            self.text[t]=remove_special_case(self.text[t])
            self.unStemmed_text[t]=remove_hyphen(self.unStemmed_text[t])
            self.unStemmed_text[t]=remove_special_case(self.unStemmed_text[t])
            #print "self.text[t] ", self.text[t]
            gram_length= len(self.text[t].split())
            token=(self.text[t]).split()
            token_Unstemmed=(self.unStemmed_text[t]).split()
            self.extract_grams(token,token_Unstemmed, int(max_gram))
#            if float(gram_length)>=1.0 and float(gram_length)<=float(max_gram) and self.text[t] not in vid_stopwords and stop_word_check(self.text[t]):
#                if self.text[t] not in (self.cand_phrase).keys():
#                    self.cand_phrase[self.text[t]]=1
#                    if self.unStemmed_text[t] not in phrase:
#                        phrase.append(self.unStemmed_text[t])
#                        unStem_phrase.append(self.text[t]+"::"+self.unStemmed_text[t])
#                else:
#                        self.cand_phrase[self.text[t]]+=1
#            else:
#                print "gram_length ", gram_length
#                if float(gram_length)>=float(max_gram):
#                    token=(self.text[t]).split()
#                    print token
#                    self.extract_grams(token,int(max_gram))


for f in sorted(text_files):
    slideContents=""
    slideContents_unstemmed=""
    height=[]
    row_num=[]
    text=[]
    unStemmed_text=[]
    ftxt=open(folder_name+"/"+f,"r")
    content=ftxt.readlines()
    ftxt.close()
    line_number=1
    for line in content:
        data=line.split("::")
        if len(data)==3:
            height.append(int(data[1].split(" ")[1]))
            if int(data[1].split(" ")[1])>max_height:
                max_height=int(data[1].split(" ")[1])
            text_stemText=data[2].rstrip("\n").lower()
            text.append(text_stemText.split("\s**s/")[0])
            #slideContents=slideContents+" "+text_stemText.split("\ ")[0]
            #slideContents_unstemmed=slideContents_unstemmed+" "+text_stemText.split("\ ")[1]
            unStemmed_text.append(text_stemText.split("\s**s/")[1])
            #print text_stemText.split("\ ")[1]
            #print text_stemText.split("\ ")[0]
    
    #print slideContents
    #print slideContents_unstemmed
    video.append(video_text(folder_name+"/"+f,height,text,unStemmed_text, slideContents,  slideContents_unstemmed))   

for v in video:
    v.extract_candidate_phrases()

remove_phrase_with_spl_char()
write_phrase()
	

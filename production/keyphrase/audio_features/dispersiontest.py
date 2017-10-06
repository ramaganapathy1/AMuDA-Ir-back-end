import nltk
from nltk import TokenSearcher
from dispersionmyversion60 import getDispersionValues
import re
import os
import sys

try:
    file_name=sys.argv[1]
    ufile_name=file_name.rstrip(".txt")+"_untagged.txt"
    gramfile=file_name.rstrip(".txt")+"_grams.txt"
except:
	print "Mandatory parameters not available"
	sys.exit()


transcriptFolder="keyphrase/output"
ngramsFolder="keyphrase/output"
outputFolder="keyphrase/output"


untagged_files=[ufile_name]
grams_files=[gramfile]
    
print untagged_files
print grams_files


for sfile in untagged_files:
    contentFile=open(transcriptFolder+"/"+sfile)
    rawContent=contentFile.read()
#    tokens=nltk.word_tokenize(rawContent)
    tokens=rawContent.split(" ")
    tokens_list=[]
    for t in tokens:
        if t!="":
            tokens_list.append(t)
    #print tokens_list
    
    ngramsFile=open(transcriptFolder+"/"+sfile.replace("_untagged.txt","_grams.txt"))
    tempList=ngramsFile.readlines()
    ngramsList=[]

    for t in tempList:
        ngramsList.append(t.replace("\n","").lower())

    #print ngramsList
    ngramsFile.close()
    
    print "Calculating dispersion:"
    dispersion=getDispersionValues(tokens_list,ngramsList,250,3)


    print "Writing dispersion into:"+transcriptFolder+"/"+sfile.replace("_untagged.txt","_disp.txt")
    outputfile=open(transcriptFolder+"/"+sfile.replace("_untagged.txt","_disp.txt"),"w")
    #print outputFolder+sfile.replace(".txt","_disp.txt")
    #outputfile=open(outputFolder+sfile.replace(".txt","_disp.txt"),"w")

    for k in dispersion.keys():
        outputfile.write(k+"::%.10f\n" % dispersion[k])

    outputfile.close()
    contentFile.close()


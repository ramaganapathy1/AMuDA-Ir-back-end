#Sample Command: python ml_audio/Naive_Bayes/ICMR_NaiveBayesStudy.py <TrainingDataSet> <test data>
#e.g.1 : python ml_audio/Naive-Bayes/ICMR_NaiveBayesStudy.py trainingData.tab CG1.txt

import orange 
import os
import sys
import icmr_nbdisc #import  icmr_nbdisc.py

try:
    feature=[]
    trained_file_name=sys.argv[1] #<TrainingDataSet>
    print trained_file_name
    test_file_name=sys.argv[2].split(".txt")[0]+".tab" #<test data>
    print test_file_name
    input_folder="output"
    complete_file_path=input_folder+"/"+test_file_name
    print complete_file_path
    handle=open(complete_file_path,"r")
    head=(handle.readlines())[0]
    head_list=head.split("\t")
    for h in head_list:
        if (h.strip()!="keyphrase" and h.strip()!="keyword"):
            feature.append(h)	
    handle.close()
    output_folder="output"
    output_file_name=test_file_name.split(".tab")[0]+".txt"
    output_file=output_folder+"/"+output_file_name
    print "Output_file:"+output_file

except:
	print "Mandatory parameters not available"
	sys.exit()

#Constructing classifier
data=orange.ExampleTable(trained_file_name)
classifier = icmr_nbdisc.Learner(data)

#Constructing classifier without cscore and dispersion values
newdomain=orange.Domain([data.domain["tfidf"],  data.domain["cuewords"], data.domain["localspan"],data.domain["Frequency Occurance Ratio"],data.domain["Contiguous Occurance Ratio"],data.domain["Phrase Size"]], data.domain.classVar)
newdata_withoutCscore_disp = orange.ExampleTable(newdomain, data)
classifier_withoutCscore_disp = icmr_nbdisc.Learner(newdata_withoutCscore_disp)


keyphrases=[]
headings=[]
headings_firstrow=[]
NotOnegramtestdata=[]
Onegramtestdata=[]
complete_file_path=input_folder+"/"+test_file_name

#Spliiting up of testdata into one gram and above one gram test data set
if (os.path.exists(complete_file_path)):
    handler=open(complete_file_path , "r")
    contents=handler.readlines()
    handler.close()
    for j in range(len(contents)):
            if j<3:
                if j==0:
                    headings_firstrow=(contents[j].rstrip("\n").split("\t"))
                headings.append(contents[j].rstrip("\n"))
            else:
                Testdata=contents[j].split("\t")[0]
                TestdataArray=Testdata.split(" ")
                if len(TestdataArray)!=1:
                    NotOnegramtestdata.append(contents[j].rstrip("\n"))
                elif len(TestdataArray)==1:
                    Onegramtestdata.append(contents[j].rstrip("\n"))

#Creating two seperate test data set
file_testdatawithoutonegrams=open(complete_file_path.rstrip(".tab")+"_withoutonegram.tab","w")
for h in headings:
    file_testdatawithoutonegrams.write(h+"\n")
for n in NotOnegramtestdata:
    file_testdatawithoutonegrams.write(n+"\n")
file_testdatawithoutonegrams.close()

file_testdatawithonegrams=open(complete_file_path.rstrip(".tab")+"_withonegram.tab","w")
for h in headings:
    file_testdatawithonegrams.write(h+"\n")
for o in Onegramtestdata:
    file_testdatawithonegrams.write(o+"\n")
file_testdatawithonegrams.close()
        
#Performing keyphrase extraction for 2,3,4 grams 
data_test=orange.ExampleTable(complete_file_path.rstrip(".tab")+"_withoutonegram.tab")
print "------------------------------------- Test Results-----------withoutonegram--------------------------"
for d in data_test:
    keyphrases_strformat=""
    v, p=classifier(d)
    if str(v)=="True":
        #print d,  p[1]
        keyphrases_strformat=keyphrases_strformat+str(d["keyphrase"])+"\t"
        for ff in feature:
            keyphrases_strformat=keyphrases_strformat+str(d[ff])+"\t"
        keyphrases.append(keyphrases_strformat)
    else:
        dummy=0

#Performing keyphrase extraction for one gram
data_test_onegram=orange.ExampleTable(complete_file_path.rstrip(".tab")+"_withonegram.tab") 
print "------------------------------------- Test Results------withonegram-------------------------------"
for d in data_test_onegram:
    keyphrases_strformat=""
    try:
        v, p=classifier_withoutCscore_disp(d)
        if str(v)=="True":
            #print d,  p[1]
            keyphrases_strformat=keyphrases_strformat+str(d["keyphrase"])+"\t"
            for ff in feature:
                keyphrases_strformat=keyphrases_strformat+str(d[ff])+"\t"
            keyphrases.append(keyphrases_strformat)
        else:
            dummy=0
    except:
        continue

keyphrases_dict={}
for k in keyphrases:
    keyphrases_dict[k.split("\t")[0]]=k

print "------------------------------------- Test Results------final-------------------------------"
for k in keyphrases_dict.keys():
    print keyphrases_dict[k]

#Writing extracted keyphrases into a <transcript_name>.txt file
f_output=open(output_file,"w")
f_output.write("keyphrase\t")
for ff in feature:
    f_output.write(ff+"\t")
f_output.write("\n")
f_output.write("\n")
for k in keyphrases_dict.keys():
    f_output.write(keyphrases_dict[k]+"\n")
f_output.close()

os.system("rm "+complete_file_path.rstrip(".tab")+"_withonegram.tab")
os.system("rm "+complete_file_path.rstrip(".tab")+"_withoutonegram.tab")


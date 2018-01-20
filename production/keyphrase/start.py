import os
li = []
path=os.getcwd()
fd = open(path+"/keyphrase/start.sh", "w+")
f=[]
for file1 in os.listdir(path+"/JVcode/Scripts/ForClassification"):
    if file1.endswith(".tab.scores"):
            f.append(file1[:-11])
for file in os.listdir(path+"/keyphrase/transcript"):
    if file.endswith(".txt"):
        if file[:-4] not in f:
            name = "./keyphrase/keyphrase.sh a " + file + " Porter_Stemmer disable none 4 'tfidf,dispersion,cscore' all_features.tab \n \n"
            print(name)
            fd.write(name)

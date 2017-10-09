import os
li = []
path=os.getcwd()
fd = open(path+"/keyphrase/start.sh", "w+")
for file in os.listdir(path+"keyphrase/transcript"):
    if file.endswith(".txt"):
        name = "./"+path+"keyphrase/keyphrase.sh a " + file + " Porter_Stemmer disable none 4 'tfidf,dispersion,cscore' all_features.tab \n \n"
        print(name)
        fd.write(name)

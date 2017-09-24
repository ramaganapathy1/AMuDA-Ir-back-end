import os
li = []
fd = open("start.sh", "w+")
for file in os.listdir("/home/ramaganapathy1/Documents/Project Latest/keyphrase/transcript/"):
    if file.endswith(".txt"):
        name = "bash ./keyphrase/keyphrase.sh a " + file + " Porter_Stemmer disable none 4 'tfidf,dispersion,cscore' all_features.tab \n"
        print(name)
        fd.write(name)

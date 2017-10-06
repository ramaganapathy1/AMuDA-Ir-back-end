import os
li = []
fd = open("keyphrase/start.sh", "w+")
for file in os.listdir("keyphrase/transcript"):
    if file.endswith(".txt"):
        name = "./keyphrase/keyphrase.sh a " + file + " Porter_Stemmer disable none 4 'tfidf,dispersion,cscore' all_features.tab \n \n"
        print(name)
        fd.write(name)

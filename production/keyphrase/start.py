import os
li = []
fd = open("start.sh", "w+")
for file in os.listdir("/Users/orion/Documents/AMuDA-Ir-back-end/production/keyphrase/transcript"):
    if file.endswith(".txt"):
        name = "./production/keyphrase/keyphrase.sh a " + file + " Porter_Stemmer disable none 4 'tfidf,dispersion,cscore' all_features.tab \n \n"
        print(name)
        fd.write(name)

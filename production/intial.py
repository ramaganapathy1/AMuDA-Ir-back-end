import os
fd=open("start.sh","w+")
path =os.getcwd()
f=[]
for file1 in os.listdir(path+"/JVcode/Scripts/ForClassification"):
    if file1.endswith(".tab.scores"):
            f.append(file1[:-11])
path=path[:-10]
print path
for i in os.listdir(path+"uploads"):
    if i.endswith(".pdf"):
        if i[:-4] not in f:
            name = "pdftotext "+path+"uploads/"+i+" "+path+"/production/keyphrase/transcript/"+i[:-3]+"txt\n"
            print (name)
            fd.write(name)
            name = ""
fd.close()
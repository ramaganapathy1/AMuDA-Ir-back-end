import os
fd=open("start.sh","w+")
path =os.getcwd()
path=path[:-10]
print path
for i in os.listdir(path+"uploads"):
    if i.endswith(".pdf"):
        name="pdftotext "+path+"uploads/"+i+" "+path+"/production/keyphrase/transcript/"+i[:-3]+"txt\n"
        print (name)
        fd.write(name)
        name=""
fd.close()
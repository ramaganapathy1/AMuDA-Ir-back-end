import os
fd=open("start.sh","w+")
path =os.getcwd()
for i in os.listdir("../uploads"):
    if i.endswith(".pdf"):
        name="pdftotext ../uploads/"+i+" "+path+"/keyphrase/transcript/"+i[:-3]+"txt\n"
        print (name)
        fd.write(name)
        name=""
fd.close()
import os
fd=open("start.sh","w+")
for i in os.listdir("/Users/orion/Documents/AMuDA-Ir-back-end/uploads"):
    if i.endswith(".pdf"):
        name="pdftotext /Users/orion/Documents/AMuDA-Ir-back-end/uploads/"+i+ " keyphrase/transcript/"+i[:-3]+"txt\n"
        print (name)
        fd.write(name)
        name=""
fd.close()
import continuityScore
import elaborationScore
#import applicationScore
import os
path=os.getcwd()+"/production/JVcode/Scripts"

listOfFiles = []

#for eachfile in os.listdir(os.getcwd()+"/tabfiles"): #tabfiles - folder with original tabfiles
#for eachfile in os.listdir("/home/ramyananth/Desktop/RAMA IR/JV"):
for eachfile in os.listdir(path+"/tabfiles/"):
    #if(eachfile.endswith(".tabn")):
    if(eachfile.endswith(".tab")):
        listOfFiles.append(eachfile)
        
for eachfile in listOfFiles:
    newDoc = open(path+"/ForClassification/"+eachfile+".scores","w") #result folder
    for everyfile in listOfFiles:
        scorec = continuityScore.getcommongrams(path+"/splitTabFiles/"+eachfile,path+"/splitTabFiles/"+everyfile)
        scoree = elaborationScore.getcommongrams(path+"/splitTabFiles/"+eachfile,path+"/splitTabFiles/"+everyfile)
        #scorea = applicationScore.getcommongrams(os.getcwd()+"/splitTabFiles/"+eachfile,os.getcwd()+"/splitTabFiles/"+everyfile)
        newDoc.write(eachfile+" "+everyfile+" "+str(scorec)+" "+str(scoree)+"\n")
    newDoc.close() #splitTabFiles - folder with the split tab files (output of split.py)

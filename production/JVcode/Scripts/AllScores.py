import continuityScore
import elaborationScore
#import applicationScore
import os

listOfFiles = []

#for eachfile in os.listdir(os.getcwd()+"/tabfiles"): #tabfiles - folder with original tabfiles
#for eachfile in os.listdir("/home/ramyananth/Desktop/RAMA IR/JV"):
for eachfile in os.listdir(os.getcwd()+"/tabfiles/"):
    #if(eachfile.endswith(".tabn")):
    if(eachfile.endswith(".tab")):
        listOfFiles.append(eachfile)
        
for eachfile in listOfFiles:
    newDoc = open(os.getcwd()+"/ForClassification/"+eachfile+".scores","w") #result folder
    for everyfile in listOfFiles:
        scorec = continuityScore.getcommongrams(os.getcwd()+"/splitTabFiles/"+eachfile,os.getcwd()+"/splitTabFiles/"+everyfile)
        scoree = elaborationScore.getcommongrams(os.getcwd()+"/splitTabFiles/"+eachfile,os.getcwd()+"/splitTabFiles/"+everyfile)
        #scorea = applicationScore.getcommongrams(os.getcwd()+"/splitTabFiles/"+eachfile,os.getcwd()+"/splitTabFiles/"+everyfile)
        newDoc.write(eachfile+" "+everyfile+" "+str(scorec)+" "+str(scoree)+"\n")
    newDoc.close() #splitTabFiles - folder with the split tab files (output of split.py)

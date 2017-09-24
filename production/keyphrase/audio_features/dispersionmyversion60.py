#this version inds the disperison using the VMR/Fano factor and the formula is
#dispersion=1/VMR+1 where in VMR variance and mean are for the frequency of terms in each fixed window of size windowSize

import numpy as np

def calculateDispersion(fanoFrequencyList):
    variance=float(np.var(np.array(fanoFrequencyList)))
    mean=float(np.mean(np.array(fanoFrequencyList)))
    if (variance+mean)!=0:
        return float(mean/(variance+mean))
    else:
        return float(0.0)

def occuringWindows(positionsList,totWindows,windowSize):
    occuringWindow=0
    curPosition=0

    for i in range(0,(totWindows*windowSize)-windowSize,windowSize):

        #if the term is occuring in the particular window
        if curPosition < len(positionsList) and positionsList[curPosition] > i and positionsList[curPosition] <= i+windowSize:
            #print "Occuring in:",i
            
            occuringWindow+=1
            while curPosition < len(positionsList) and i+windowSize >= positionsList[curPosition]:
                curPosition+=1
                
      
    return occuringWindow
    
def fanoFrequency(positionsList,totWindows,windowSize):
    fanoPositions=[]
    occuringWindow=0
    curPosition=0

    for i in range(0,(totWindows*windowSize)-windowSize,windowSize):

        #if the term is occuring in the particular window
        if curPosition < len(positionsList) and positionsList[curPosition] > i and positionsList[curPosition] <= i+windowSize:
            #print "Occuring in:",i
            
            tempTerm=0
            while curPosition < len(positionsList) and i+windowSize >= positionsList[curPosition]:
                curPosition+=1
                tempTerm+=1

            
            fanoPositions.append(tempTerm)
        else:
            fanoPositions.append(0)
    return fanoPositions

def getPositions(stemmedTokens,keywordsList):
    
    positions={}
    size=len(stemmedTokens)
    for k in keywordsList:
        
        if k in positions.keys():
            continue

        #print k
        m=len(k.split())

        #poss=[1]
        poss=[]
        for i in range(size-m-1):
            word=""

            for j in range(m):
                word+=stemmedTokens[i+j]+" "
            word=word.rstrip(" ")

            #print "word:",word
            if k==word:
                poss.append(i+1)

        
        positions[k]=poss

##        #if only one position it will be eliminated and no need to check its position so continue the loop
##        if len(positions[k])<=1:
##            continue
##        #if first and second item in the list is 1 then remove one item cause the word itself is in the first position
##        if (positions[k])[0]==(positions[k])[1]:
##            positions[k].remove(1)
##            #print k+" is first word"
##
##        #add the last interval only if the word is not in the last
##        if not (positions[k])[len(positions[k])-1] == len(stemmedTokens)- len(k)-2:
##            positions[k].append(len(stemmedTokens)- len(k)-2)
            
    return positions



def getDispersionValues(stemmedTokens,keywordsList,windowSize,maxOccurrence):
    
    totWindowsCount=len(stemmedTokens)/windowSize

    if len(stemmedTokens) % windowSize > 0:
        totWindowsCount+=1


    positions=getPositions(stemmedTokens,keywordsList)
    #if reminder is there add another one
    
    #keys contains atleast n positions making it easier to calculate the dispersion
    
    keys=[k for k in positions.keys() if (len(positions[k])> maxOccurrence)]

    #print "keys",keys
    
    #nonkeys will have dispersion value as zero
    nonkeys=[k for k in positions.keys() if  (len(positions[k])<=maxOccurrence)]
    
    dispersion={}

    for k in keys:

        #get the fano positions.. fano positions is freq of terms present in each positions
        #print k.replace(" ","-"),":",positions[k],":",range(0,totWindowsCount*windowSize,windowSize),":",fanoFrequency(positions[k],totWindowsCount,windowSize),":",calculateDispersion(fanoFrequency(positions[k],totWindowsCount,windowSize)),":",occuringWindows(positions[k],totWindowsCount,windowSize),":",totWindowsCount
        dispersion[k]=calculateDispersion(fanoFrequency(positions[k],totWindowsCount,windowSize))
        #dispersion[k]=calculateDispersion(fanoFrequency(positions[k],totWindowsCount,windowSize))

    #add nonkeys dispersion 0 also
    for k in nonkeys:
        dispersion[k]=0.0
    
    return dispersion

        
        


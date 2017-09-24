#<testing> : accepts <transcript_name>.txt as input from user
#<trainingData> :  accepts <trainingData>.tab as input from user 

testing=$1
trainingData=$2


python ml_audio/Naive-Bayes/ICMR_NaiveBayesStudy.py $trainingData $testing



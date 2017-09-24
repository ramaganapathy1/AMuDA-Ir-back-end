testing_list=$1
trainingData=$2

echo "Keyphrase extraction"

for testing in $testing_list; do 
	echo $testing
	python ml_audio/Naive-Bayes/ICMR_NaiveBayesStudy.py $trainingData $testing
	echo "done"
done

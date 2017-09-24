testing_list=$1
trainingData=$2
dot="_"
one_g="1gram"
two_g="2gram"
three_g="3gram"
four_g="4gram"
tab=".tab"

echo "Keyphrase extraction"

for testing in $testing_list; do 
	echo $testing
	td="$trainingData$dot$one_g$tab"
	t="$testing$dot$one_g"
	python ml_audio/Naive-Bayes/Naive-Bayes.py $td $t 
	echo $td
	echo $t
	td="$trainingData$dot$two_g$tab"
	t="$testing$dot$two_g"
	python ml_audio/Naive-Bayes/Naive-Bayes.py $td $t 
	echo $td
	echo $t
	td="$trainingData$dot$three_g$tab"
	t="$testing$dot$three_g"
	python ml_audio/Naive-Bayes/Naive-Bayes.py $td $t 
	echo $td
	echo $t
	td="$trainingData$dot$four_g$tab"
	t="$testing$dot$four_g"
	python ml_audio/Naive-Bayes/Naive-Bayes.py $td $t 
	echo $td
	echo $t
	echo "done"
done

testing_list=$1

echo "Corr Impact"

for testing in $testing_list; do 
	echo $testing
	python ml_audio/Naive-Bayes/corrImpact.py $testing
	echo "done"
done

transcript_list=$1

echo "evaluation Gramwise"

for transcript in $transcript_list; do 
	echo $transcript
	python evaluationGramwise.py $transcript Porter-Stemmer
	echo "done"
done

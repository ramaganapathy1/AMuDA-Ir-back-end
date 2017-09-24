transcript_list=$1

echo "evaluation"

for transcript in $transcript_list; do 
	echo $transcript
	python evaluation.py $transcript Porter-Stemmer
	echo "done"
done

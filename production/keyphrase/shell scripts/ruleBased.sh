transcript_list=$1

echo "After applying rules"

for transcript in $transcript_list; do 
	echo $transcript
	python ruleBased.py $transcript
	echo "done"
done

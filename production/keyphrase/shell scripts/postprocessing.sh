transcript_list=$1

echo "post processing"

for transcript in $transcript_list; do 
	echo $transcript
	python postprocessing.py $transcript
	echo "done"
done

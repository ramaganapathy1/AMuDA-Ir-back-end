transcript_list=$1

echo "post processing"

for transcript in $transcript_list; do 
	echo $transcript
	python postprocessing_temp.py $transcript
	echo "done"
done

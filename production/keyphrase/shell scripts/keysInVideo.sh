transcript_list=$1

echo "keys "

for transcript in $transcript_list; do 
	echo $transcript
	python keysInVideo.py $transcript
	echo "done"
done

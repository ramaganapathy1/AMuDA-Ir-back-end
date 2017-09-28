transcript_list=$1
gramSize=$2

for transcript in $transcript_list; do 
	python production/keyphrase/preprocess_video/extractgrams.py $transcript $gramSize
done




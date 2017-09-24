transcript_list=$1
stemmer=$2
gramSize=$3

for transcript in $transcript_list; do 
	python keyphrase/audio_features/cue.py  $transcript $stemmer $gramSize
done





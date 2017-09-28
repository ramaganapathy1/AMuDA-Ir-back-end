transcript_list=$1
gramSize=$2
stemmer=$3

for transcript in $transcript_list; do 
	python production/keyphrase/audio_features/localspan.py $transcript $gramSize $stemmer
done





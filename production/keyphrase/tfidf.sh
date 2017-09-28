stemmer=$1
gramSize=$2
transcript_list=$3

for transcript in $transcript_list; do 
	python production/keyphrase/audio_features/tfidf.py $stemmer $gramSize $transcript
done

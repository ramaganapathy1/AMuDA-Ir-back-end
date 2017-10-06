transcript_list=$1
stemmer=$2

for transcript in $transcript_list; do 
	python keyphrase/audio_features/cscore.py $transcript $stemmer
done

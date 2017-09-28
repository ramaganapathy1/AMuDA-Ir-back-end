transcript_list=$1
stemmer=$2
pos_tagging=$3

for transcript in $transcript_list; do 
	python production/keyphrase/preprocess_audio/pos.py $transcript $stemmer $pos_tagging
done

transcript_list=$1
stemmer=$2

for transcript in $transcript_list; do 
	python preprocess_video/text_stem.py $transcript $stemmer
done

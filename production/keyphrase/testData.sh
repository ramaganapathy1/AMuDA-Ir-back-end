transcript_list=$1
feature_list=$2
feature_ext=$3
stemmer=$4

for transcript in $transcript_list; do 
	python keyphrase/ml_audio/testData/write.py $transcript $feature_list $feature_ext $stemmer
done

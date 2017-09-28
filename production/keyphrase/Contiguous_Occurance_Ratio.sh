transcript_list=$1
ext=$2

for transcript in $transcript_list; do 
	python production/keyphrase/video_features/contiguous_count_ratio.py $transcript $ext
done

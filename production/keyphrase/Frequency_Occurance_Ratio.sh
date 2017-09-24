transcript_list=$1
ext=$2

for transcript in $transcript_list; do 
	python keyphrase/video_features/freq_occur_ratio.py $transcript $ext
done

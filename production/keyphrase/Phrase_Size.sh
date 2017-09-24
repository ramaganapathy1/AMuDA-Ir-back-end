transcript_list=$1
inputfolder=$2
outputfolder=$3
ext=$4

for transcript in $transcript_list; do 
	python keyphrase/video_features/max_height.py $transcript $inputfolder $outputfolder $ext
done

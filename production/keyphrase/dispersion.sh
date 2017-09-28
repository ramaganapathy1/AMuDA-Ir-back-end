transcript_list=$1

for transcript in $transcript_list; do 
	python production/keyphrase/audio_features/dispersiontest.py $transcript
done


#!/usr/bin/env bash
mode=$1
transcript_name=$2
stemmer_name=$3
pos_status=$4
pos_filter_file=$5
max_gram=$6
status="disable"
train_file=$8




if [ "$mode" == "av" ] || [ "$mode" == "a" ]
then
	echo "Pre-Processing Audio Transcript"
		./keyphrase/pos.sh $transcript_name $stemmer_name $pos_status
	if [ "$pos_status" == "enable" ] 
	then
		./keyphrase/grams_pos.sh $transcript_name $max_gram $pos_filter_file $stemmer_name
	else
		./keyphrase/grams.sh $transcript_name $max_gram none $stemmer_name
	fi
	echo "Done -- Pre-Processing Audio Transcript"
fi

if [ "$mode" == "av" ] || [ "$mode" == "v" ]
then
	echo "Pre-Processing Text Area of Video"
	python keyphrase/text_stem.py $transcript_name $stemmer_name
	python keyphrase/extractgrams.py $transcript_name $max_gram
	echo "Done - Pre-Processing Text Area of Video"
fi

feature_list=$7
feature_ext=""
comma_str=","
export IFS=","

if [ "$mode" == "av" ] || [ "$mode" == "a" ] || [ "$mode" == "v" ]
then
	for feature in $feature_list; do
	  if [ "$feature" == "cscore" ] &&  [ "$mode" == "a" -o "$mode" == "av" ]
	  then
		echo "Cscore"
		bash ./keyphrase/cscore.sh $transcript_name $stemmer_name
		ext="_cscore.txt"
		feature_ext=${feature_ext}${ext}${comma_str}
	  fi
	  if [ "$feature" == "localspan" ] &&  [ "$mode" == "a" -o "$mode" == "av" ]
	  then
		echo "Localspan"
		bash ./keyphrase/localspan.sh $transcript_name $stemmer_name $max_gram
		ext="_localspan.txt"
		feature_ext=${feature_ext}${ext}${comma_str}
	  fi
	  if [ "$feature" == "cuewords" ] &&  [ "$mode" == "a" -o "$mode" == "av" ]
	  then
		echo "Cuewords"
		bash ./keyphrase/cue.sh $transcript_name $stemmer_name $max_gram
		ext="_cue.txt"
		feature_ext=${feature_ext}${ext}${comma_str}
	  fi
	  if [ "$feature" == "tfidf" ] &&  [ "$mode" == "a" -o "$mode" == "av" ]
	  then
		echo "TF-IDF"
		bash ./keyphrase/tfidf.sh $stemmer_name $max_gram $transcript_name
		ext="_tfidf.txt"
		feature_ext=${feature_ext}${ext}${comma_str}
	  fi
	  if [ "$feature" == "dispersion" ] &&  [ "$mode" == "a" -o "$mode" == "av" ]
	  then
		echo "Dispersion"
		bash ./keyphrase/dispersion.sh $transcript_name $max_gram $stemmer_name
		ext="_disp.txt"
		feature_ext=${feature_ext}${ext}${comma_str}
	  fi
	  if [ "$feature" == "cont_ratio" ] &&  [ "$mode" == "v" -o "$mode" == "av" ]
	  then
		echo "Contiguous_Occurance_Ratio"
		ext="_cont.txt"
		python keyphrase/video_features/contiguous_count_ratio.py $transcript_name $ext
		feature_ext=${feature_ext}${ext}${comma_str}
	  fi
	 if [ "$feature" == "freq_ratio" ] &&  [ "$mode" == "v" -o "$mode" == "av" ]
	  then
		echo "Frequency Occurance Ratio"
		ext="_freq.txt"
		python keyphrase/video_features/freq_occur_ratio.py $transcript_name $ext
		feature_ext=${feature_ext}${ext}${comma_str}
	  fi
	done
fi
feature_ext="'"${feature_ext}"'"

export IFS=" "

echo "Integrating all feature results"
str="python keyphrase/write.py "$transcript_name" "$feature_list" "$feature_ext" "$stemmer_name
python keyphrase/ml_audio/write.py $transcript_name $feature_list $feature_ext $stemmer_name
#echo "$str"



transcript_list=$1

echo "tfidf Generation"
echo $transcript_list
echo "After replecement"
transcript_list_new={$transcript_list// /,}

python audio_features/tfidf.py "Porter-Stemmer" 4 $transcript_list_new
echo "done"


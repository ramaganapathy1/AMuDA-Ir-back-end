from nltk import stem
def stem_token_function(stemmer_name,word):
	stem_token=""
	if stemmer_name=="Porter-Stemmer":
		#print ("Performing Porter Stemming")
		stemmer = stem.PorterStemmer()
		phrase_array_token=word.split()
		stem_token=""
		for s in phrase_array_token:
			stem_token=stem_token+stemmer.stem(s)+" "
		stem_token=stem_token.strip(" ")
		word=stem_token
	elif stemmer_name=="Lancaster-Stemmer":
		#print ("Performing Lancaster Stemming")
		stemmer = stem.LancasterStemmer()
		phrase_array_token=word.split()
		stem_token=""
		for s in phrase_array_token:
			stem_token=stem_token+stemmer.stem(s)+" "
		stem_token=stem_token.strip(" ")
		word=stem_token
	elif stemmer_name=="WordNet-Lemmatizer":
		#print ("Performing Wordnet Lemmatization")
		stemmer = WordNetLemmatizer()
		phrase_array_token=word.split()
		stem_token=""
		for s in phrase_array_token:
			stem_token=stem_token+stemmer.lemmatize(s)+" "
		stem_token=stem_token.strip(" ")
		word=stem_token
			#stopword[count]=stemmer.lemmatize(stopword[count])
	return(word)

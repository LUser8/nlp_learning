from nltk.stem import PorterStemmer, RegexpStemmer, SnowballStemmer

words=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized", "Congratulations", 
       "Fairly", "Sportingly", "goes"]

### Porter Stemmer
stemming=PorterStemmer()
print("---- Porter Stemmer")
for word in words:
    print(word, '---->', stemming.stem(word))

### Regexp Stemmer
reg_stemmer=RegexpStemmer('ing$|s$|e$|able$', min=4)
print("\n---- Regexp Stemmer")
for word in words:
    print(word, '---->', reg_stemmer.stem(word))

### Snowball Stemmer (Porter2)
snowball_stemmer = SnowballStemmer('english')
print("\n---- Snowball Stemmer")
for word in words:
    print(word, '---->', snowball_stemmer.stem(word))

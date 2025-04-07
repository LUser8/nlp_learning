# import nltk 
# nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer


words=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized", "Congratulations", 
       "Fairly", "Sportingly", "goes"]


lemmatizer = WordNetLemmatizer()

print("\n---- WordNetLemmatizer")
for word in words:
    print(word, '---->', lemmatizer.lemmatize(word, pos='n'))

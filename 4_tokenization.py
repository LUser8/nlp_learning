
# import nltk
# nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.tokenize import TreebankWordTokenizer

corpus = """Welcome! Hello my name is Atul. 
I am a software developer. You are watching atul's code.
My specification in python language, I love to coding.
"""

### Tokenization - paragraph to sentenses 
documents = sent_tokenize(corpus)
print(documents) 

### Tokenization - sentences to words
words = word_tokenize(corpus)
print(words)

### Tokenization - sentences to words
words = wordpunct_tokenize(corpus)
print("---- wordpunct_tokenize ----")
print(words)

### TreeBankWordTokenizer
print("---- TreebankWordTokenizer ----")
tokenizer = TreebankWordTokenizer()
words = tokenizer.tokenize(corpus)
print(words)
import nltk
import numpy
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
nltk.download('maxent_ne_chunker_tab')




sentence="The Eiffel Tower was built from 1887 to 1889 by Gustave Eiffel, whose company specialized in building metal frameworks and structures."
words=nltk.word_tokenize(sentence)
tag_elements=nltk.pos_tag(words)
print(nltk.ne_chunk(tag_elements))
nltk.ne_chunk(tag_elements).draw()

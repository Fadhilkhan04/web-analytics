from nltk.tokenize import word_tokenize, sent_tokenize

text = """Natural Language Toolkit (NLTK) is one of the largest Python libraries for performing various Natural Language Processing tasks. 
From rudimentary tasks such as text pre-processing to tasks likes vectorized representation of text – NLTK’s API has covered everything."""

sentences = sent_tokenize(text)
words = word_tokenize(text)

print("Sentence Tokenization:", sentences)
print("Word Tokenization:", words)

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize


nltk.download('punkt')

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()


sentences = sent_tokenize(text)
print("Sentence Tokenization:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")

words = word_tokenize(text)
print("\nWord Tokenization:")
print(words)

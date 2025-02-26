import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')


with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()


words = word_tokenize(text)


stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed = [stemmer.stem(word) for word in words]
lemmatized = [lemmatizer.lemmatize(word) for word in words]


print("Stemmed:", stemmed)
print("\nLemmatized:", lemmatized)

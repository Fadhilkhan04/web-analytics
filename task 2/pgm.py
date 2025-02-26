import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')


with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()


words = word_tokenize(text)


stop_words = set(stopwords.words('english'))


filtered_words = [word for word in words if word.lower() not in stop_words]

print("Original Words:")
print(words)

print("\nFiltered Words (Without Stop Words):")
print(filtered_words)

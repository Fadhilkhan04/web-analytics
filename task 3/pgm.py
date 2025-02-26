import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = text.lower()


words = word_tokenize(text)

stop_words = set(stopwords.words('english'))


filtered_words = [word for word in words if word not in stop_words and word not in string.punctuation]

print("Filtered Words (Lowercase, No Stop Words, No Punctuation):")
print(filtered_words)

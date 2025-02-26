import re


with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)


cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

print("Cleaned Text:")
print(cleaned_text)

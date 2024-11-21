import string
def get_first_sentence(text):
    sentence_endings = ['.', '!', '?']
    for ending in sentence_endings:
        sentence_end_idx = text.find(ending)
        if sentence_end_idx != -1:
            return text[:sentence_end_idx + 1]
    return text

def sort_words(words):
    ukr_words = sorted([word for word in words if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in word)], key=lambda s: s.lower())
    eng_words = sorted([word for word in words if any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in word)], key=lambda s: s.lower())
    return ukr_words + eng_words

try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()

        first_sentence = get_first_sentence(text)
        print("Перше речення:", first_sentence)

        translator = str.maketrans('', '', string.punctuation)
        words = text.translate(translator).split()
        print('Слова: ', words)
        sorted_words = sort_words(words)
        print('Відсортовані слова: ', sorted_words)
        print('Кількість слів: ', len(words) )
except FileNotFoundError:
    print("Помилка: Файл не знайдено.")
except Exception as e:
        print(f"Виникла помилка: {e}")
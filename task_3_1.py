def num_translate(number):
    word_base = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    print(word_base.get(number, 'число больше десяти'))



num_translate(number=input('Введите прописью число от 1 до 10 на английском языке: '))




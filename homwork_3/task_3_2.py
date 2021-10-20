def num_translate(numbers):
    word_base = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if numbers.lower() != numbers:
        number = word_base.get(numbers.lower(), None)
        if number == None:
            return None
        else:
            return number.title()
    else:
        return (word_base.get(numbers, None))

print(num_translate('Two'))
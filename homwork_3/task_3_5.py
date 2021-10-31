
def get_jokes(n):
    """
    generate a joke

    :param n: number of jokes
    :return: joke list
    """
    number_of_jokes = n

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    from random import choice
    jokes = []
    i = 0
    while i < number_of_jokes:
        joke = []
        one = choice(nouns)
        joke.append(one)
        two = choice(adverbs)
        joke.append(two)
        three = choice(adjectives)
        joke.append(three)
        message = str(' '.join(joke))
        jokes.append(message)
        i +=1
    return jokes

print(get_jokes(3))



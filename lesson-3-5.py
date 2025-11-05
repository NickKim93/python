#task 5

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, flag=False):
    for i in range(n):
        random_index_1 = random.choice(nouns)
        random_index_2 = random.choice(adverbs)
        random_index_3 = random.choice(adjectives)
        one_joke = f'{random_index_1} {random_index_2} {random_index_3}'
        print(one_joke)
        if flag:
            list_1 = one_joke.split()
            for noun in nouns:
                for el in list_1:
                    if noun == el:
                        nouns.remove(noun)

            for adverb in adverbs:
                for el in list_1:
                    if adverb == el:
                        adverbs.remove(adverb)

            for adjective in adjectives:
                for el in list_1:
                    if adjective == el:
                        adjectives.remove(adjective)


get_jokes(1)

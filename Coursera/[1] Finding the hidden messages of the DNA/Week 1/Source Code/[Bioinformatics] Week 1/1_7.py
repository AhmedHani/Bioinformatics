__author__ = 'Ahmed Hani Ibrahim'


def symbol_to_number(symbol):
    if symbol == 'A':
        return 0
    if symbol == 'C':
        return 1
    if symbol == 'G':
        return 2
    if symbol == 'T':
        return 3


def number_to_symbol(number):
    if number == 0:
        return 'A'
    if number == 1:
        return 'C'
    if number == 2:
        return 'G'
    if number == 3:
        return 'T'


def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0

    symbol = pattern[len(pattern)-1]
    prefix = pattern[0:len(pattern)-1]

    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)

def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)

    prefix_index = int(index / 4)
    remainder = index % 4
    symbol = number_to_symbol(remainder)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)

    return prefix_pattern + symbol

def find_frequent_words_by_sorting(text, k):
    frequent_patterns = []
    indices = []
    count = []

    for i in range(0, len(text) - k):
        pattern = text[i:(i+k)]
        indices.append(pattern_to_number(pattern))
        count.append(1)

    indices.sort()

    for i in range(1, len(text) - k):
        if indices[i] == indices[i - 1]:
            count[i] = count[i - 1] + 1

    max_count = max(count)


    for i in range(0, len(text) - k):
        if count[i] == max_count:
            pattern = number_to_pattern(indices[i], k)
            frequent_patterns.append(pattern)

    return frequent_patterns

print(" ".join(map(lambda v: str(v), find_frequent_words_by_sorting("AGTCA", 2))))
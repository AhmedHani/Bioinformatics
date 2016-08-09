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


print(pattern_to_number('CTTTGCGGAGCACGGC'))
print(number_to_pattern(7369, 8))
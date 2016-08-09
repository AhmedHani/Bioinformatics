__author__ = 'Ahmed Hani Ibrahim'
import sys
import math
lines = sys.stdin.read().splitlines()

def Count(text, pattern):
    count = 0

    for i in range(0, len(text)):
        if text[i:(i + len(pattern))] == pattern:
            count += 1

    print(count)

def pattern_count(text, pattern):
    count = start = 0

    while True:
        start = text.find(pattern, start) + 1
        if start > 0:
            count += 1
        else:
            return count

def frequent_word(text, k):
    frequent_patterns = []
    count = []

    for i in range(0, len(text) - k):
        pattern = text[i:(k + i)]
        count.append(pattern_count(text, pattern))

    max_count = max(count)

    for i in range(0, len(text) - k):
        if count[i] == max_count:
            frequent_patterns.append(text[i:(k + i)])

    return frequent_patterns

unique = set(frequent_word(lines[0], int(lines[1])))
unique_list = list(unique)

res = ""

for i in range(0, len(unique_list)):
    res += str(unique_list[i]) + " "

print(res)


def reverse(text):
    return text[::-1]

def complement(text):
    new_text = ""

    for i in range(0, len(text)):
        if text[i] == 'A':
            new_text += 'T'
        elif text[i] == 'G':
            new_text += 'C'
        elif text[i] == 'T':
            new_text += 'A'
        elif text[i] == 'C':
            new_text += 'G'
        elif text[i] == 'G':
            new_text += 'C'

    return new_text

def pattern_to_number(pattern):
    max_power = len(pattern) - 1
    res = 0

    for i in range(0, len(pattern)):
        if pattern[i] == 'A':
            res += (0 * math.pow(4, max_power))
        elif pattern[i] == 'C':
            res += (1 * math.pow(4, max_power))
        elif pattern[i] == 'G':
            res += (2 * math.pow(4, max_power))
        else:
            res += (3 * math.pow(4, max_power))

        max_power -= 1

    return int(math.floor(res))

def number_to_symbol(number):
    if number == 0:
        return 'A'
    if number == 1:
        return 'C'
    if number == 2:
        return 'G'
    if number == 3:
        return 'T'

def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)

    prefix_index = int(index / 4)
    remainder = index % 4
    symbol = number_to_symbol(remainder)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)

    return prefix_pattern + symbol

def frequency_count(text, k):
    freq_array = [0 for i in range(0, 4**k)]

    for i in range(0, len(text) - (k - 1)):
        pattern = text[i:(k + i)]
        number = pattern_to_number(pattern)
        freq_array[number] += 1

    return freq_array

res_lis = frequency_count(lines[0], int(lines[1]))

res = ""

for i in range(0, len(res_lis)):
    res += str(res_lis[i])
    res += " "

print(res)

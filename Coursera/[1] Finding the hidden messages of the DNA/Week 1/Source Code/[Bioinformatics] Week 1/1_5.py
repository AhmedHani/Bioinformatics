__author__ = 'Ahmed Hani Ibrahim'

import math

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

def number_to_pattern(i, k):
    current = None
    pattern = ""
    while current >= k:
        remainder = i % k
        current = int(i / k)

        if remainder == '0':
            pattern += 'A'
        elif remainder == '1':
            pattern += 'C'
        elif remainder == '2':
            pattern += 'G'
        elif remainder == '3':
            pattern += 'T'

    return pattern


def frequency_count(text, k):
    freq_array = [0 for i in range(0, 4**k)]

    for i in range(0, len(text) - (k - 1)):
        pattern = text[i:(k + i)]
        number = pattern_to_number(pattern)
        freq_array[number] += 1

    return freq_array

res_lis = frequency_count('TTAGGTAATCGGTTGATGTGTGGAGTTACTCGTGTCGATACGGTGCTGGAGCACGTTAGGAGTGACGGACTAGTATAGACTTGGATGATGGAGAAAGTAATTTGAGTGAGCCCGGGCTTATTACTCACATAGCCAGTGACATGAAGCCGCTGGTTCTACGGCTCCCCCGCTCTAATCCACCGTGGAACTAGGGGCAAGGCCGTGTTCGTCTAGAAAGTAATGGAGTGCGTCGTAATTCTAATTAAGTGACCAAGCGTGAATTCCTGTTTGTGGAGCTGTATCTAGGATCAGCTATTGCGGGGCCCCCTAGCTAAGGGCCCCTTAATCTCCAGGTAGGTGCTGATCTACTAGTATTATGTGTCTTGTTATAGCCAGAGCAAAAGCCCACTTCGACACTGAGATTAGTCGATGGTTAGATCTGTAGATGAGCTCATATGCATTTTCGTTCACAGTGAGTAGCACAAGCTTATCGGATCCGGTTATAGGGCGTGATCTGCATACAGCCCAGGATAGGAATCCCGGGAATAACAAATGACGACCACGCTTGCATTGCGACCTCGAACTCGGGCGCTAGCAACTCGAATTGGGCACTAGCCTGCCGGACACCTAAATAGAACATTAACCAGCACTCGGCGGCGCCCCAGTTCCAGAGGACCCCCCAAGCCAGGAGTGGTATACCGCTCTGCATGCGGTGTTTCTTCTGAAGCTACGATAAACAAATATCATTTTCTGGGCA', 5)

print(" ".join(map(lambda v: str(v), res_lis)))

def faster_frequent_word(text, k):
    frequent_patterns = []
    frequency_array = frequency_count(text, k)
    max_count = max(frequency_array)

    for i in range(0, 4**k - 1):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, 4)
            frequent_patterns.append(pattern)

    return frequent_patterns
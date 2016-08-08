__author__ = 'Ahmed Hani Ibrahim'
#1.2 Hidden Messages in the Replication Origin

text = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
pattern = "AGTTTCGAG"
k = 11

def pattern_count(text, pattern):
    count = start = 0

    while True:
        start = text.find(pattern, start) + 1
        if start > 0:
            count += 1
        else:
            return count

#print(pattern_count(text, pattern))

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

    print(len(frequent_patterns))
    return set(frequent_patterns)

print(frequent_word(text, k))
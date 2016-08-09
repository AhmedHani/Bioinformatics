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

unique = set(frequent_word(text, k))
unique_list = list(unique)

print(" ".join(map(lambda v: str(v), unique_list)))


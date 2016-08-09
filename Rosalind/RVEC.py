___author__ = 'ahani'

'''
- Problem url: http://rosalind.info/problems/revc/
'''

from collections import Counter

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

def main():
    with open('./data/reverse_complement.txt') as f:
        input = f.read().strip()

    output = complement(reverse(input))

    print(output)

    with open('./output/reverse_complement.txt', 'w') as f:
        f.write(output)


if __name__ == '__main__':
    main()
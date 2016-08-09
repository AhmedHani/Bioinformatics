__author__ = 'ahani'

'''
- Problem url: http://rosalind.info/problems/dna/
'''

from collections import Counter


def molecules_frequency(dna_string):
    return Counter(''.join(sorted(dna_string)))

def main():
    with open('./data/rosalind_dna.txt') as f:
        dna_string = f.read().strip()

    freq = molecules_frequency(dna_string)
    res = [freq[i] for i in "ACGT"]
    res = ' '.join(map(lambda v: str(v), res))

    print(res)

    with open('./output/dna_rosalind.txt', 'w') as f:
        f.write(res)


if __name__ == '__main__':
    main()





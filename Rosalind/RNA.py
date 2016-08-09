__author__ = 'ahani'

'''
- Problem url: http://rosalind.info/problems/rna/
'''

from collections import Counter


def dna_to_rna(dna_string):
    return dna_string.replace('T', 'U')


def main():
    with open('./data/rosalind_rna.txt') as f:
        dna_string = f.read().strip()

    rna_string = dna_to_rna(dna_string)

    print(rna_string)

    with open('./output/rna_rosalind.txt', 'w') as f:
        f.write(rna_string)


if __name__ == '__main__':
    main()
___author__ = 'ahani'

'''
- Problem url: http://rosalind.info/problems/hamm/
'''

from collections import Counter


def main():
    with open('./data/hamm.txt') as f:
        input_data = f.read().split("\n")

    output = str(len(filter(lambda (u, v): u != v, zip(input_data[0], input_data[1]))))

    with open('./output/hamm.txt', 'w') as f:
        f.write(output)


if __name__ == '__main__':
    main()
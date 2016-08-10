___author__ = 'ahani'

'''
- Problem url: http://rosalind.info/problems/subs/
'''

from collections import Counter


def main():
    with open('./data/subs.txt') as f:
        input_data = f.read().split("\n")

    original = input_data[0]
    subs = input_data[1]
    indices = []
    count = 0
    index = 0

    while index <= len(original) - 1:
        current_index = index
        for i in range(0, len(subs)):
            if subs[i] == original[index]:
                count += 1
                index += 1

                if index == len(original):
                    break

        if count == len(subs):
            indices.append(current_index + 1)

        count = 0
        index = current_index + 1

    output = ' '.join(map(lambda v: str(v), indices))
    print(output)

    #output = ' '.join(map(lambda v: str(v), [(i + 1) for i in range(len(original)) if original.startswith(subs, i)]))  :P
    #print(output)

    with open('./output/subs.txt', 'w') as f:
        f.write(output)


if __name__ == '__main__':
    main()
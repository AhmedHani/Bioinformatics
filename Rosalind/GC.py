___author__ = 'ahani'

'''
- Problem url: http://rosalind.info/problems/gc/
'''

from collections import Counter

def main():
    with open('./data/gc.txt') as f:
        input = f.read().split(">")

    data = []
    selected_id = 0
    best_precentage = 0

    for i in range(1, len(input)):
        current_sample = input[i].replace('\n', '').split('\n')
        id = current_sample[0][:13]
        dna = current_sample[0][13:]
        data.append((id, dna))

    for id, genome in data:
        freq = Counter(genome)
        gc_freq = freq['G'] + freq['C']
        gc_precentage = (float(gc_freq) / float(len(genome))) * float(100.0)
        if gc_precentage > best_precentage:
            selected_id = str(id)
            best_precentage = gc_precentage

    print(selected_id)
    print(round(best_precentage, 6))

    output = str(selected_id) + "\n" + str(round(best_precentage, 6))

    with open('./output/gc.txt', 'w') as f:
        f.write(output)


if __name__ == '__main__':
    main()
___author__ = 'Ahmed Hani Ibrahim'

from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from dna import DNA
import os


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem2')
    solution_dir = os.path.join("Problems", "Problem2Solution")

    data_reader = DataReader(problem_dataset_dir)
    training_data, testing_data = data_reader.get_data()
    codons_table = data_reader.get_rna_codon_table()

    for sample in training_data:

        dna_string = sample[0][0]
        amino_acid = sample[0][1]
        output = sample[1]
        dna = DNA(dna_string)
        dna.set_codon_table(codons_table)
        candidates = dna.get_dna_to_amino_acid_candidates(amino_acid)

        if set(candidates) != set(output):
            raise Exception("Output not matched!\nExpecting: " + str(output) + "\nFound: " + str(candidates))

    print("Passed training data..\n\n")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for sample in testing_data:
        usage.start()
        dna_string = sample[0][0]
        amino_acid = sample[0][1]
        dna = DNA(dna_string)
        dna.set_codon_table(codons_table)
        candidates = dna.get_dna_to_amino_acid_candidates(amino_acid)
        usage.end()

        writer.write_data((dna_string, amino_acid), candidates, usage.get_execution_time(), usage.get_memory_usage())
        print("DNA:\n" + dna_string)
        print("Protein\n" + amino_acid)

        print("\n\nOutput")
        print("=====")

        print(str(len(candidates)))
        for substring in candidates:
            print(substring)

        print("\n\nExecution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Usage: " + str(usage.get_memory_usage()) + " MB")




if __name__ == '__main__':
    main()

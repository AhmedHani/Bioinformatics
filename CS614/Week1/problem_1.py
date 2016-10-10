___author__ = 'Ahmed Hani Ibrahim'

from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from rna import RNA
import os


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem1')
    solution_dir = os.path.join("Problems", "Problem1Solution")

    data_reader = DataReader(problem_dataset_dir)
    training_data, testing_data = data_reader.get_data()
    codons_table = data_reader.get_rna_codon_table()

    for sample in training_data:
        rna_string = sample[0]
        output = sample[1]
        rna = RNA(rna_string)
        rna.set_codons_table(codons_table)
        amino_acid = rna.to_amino_acid()

        if amino_acid != output:
            raise Exception("Output not matched!\nExpecting: " + output + "\nFound: " + amino_acid)

    print("Passed training data..\n\n")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for sample in testing_data:
        usage.start()
        rna_string = sample[0]
        rna = RNA(rna_string)
        rna.set_codons_table(codons_table)
        amino_acid = rna.to_amino_acid()
        usage.end()

        writer.write_data(rna_string, amino_acid, usage.get_execution_time(), usage.get_memory_usage())

        print("RNA:\n" + rna_string)
        print("Protein:\n" + amino_acid)
        print("\n\nExecution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Usage: " + str(usage.get_memory_usage()) + " MB")

if __name__ == '__main__':
    main()

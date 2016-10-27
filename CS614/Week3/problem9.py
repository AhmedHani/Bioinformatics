___author__ = 'Ahmed Hani Ibrahim'
from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from dna import DNA
import os
import numpy as np


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem9')
    solution_dir = os.path.join("Problems", "Problem9Solution")

    data_reader = DataReader(problem_dataset_dir)
    test_cases, output = data_reader.get_data()

    for train_i in range(0, len(output)):
        case = test_cases[train_i]
        case_output = output[train_i]
        genome = case[0]
        k = case[1][0]
        d = case[1][1]
        dna = DNA(genome)
        k_mers = dna.most_frequent_missmatched_k_mer(int(k), int(d))

        if case_output.sort() != k_mers.sort():
            raise Exception("Output not matched!\nExpecting: " + str(case_output) + "\nFound: " + str(k_mers))

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()


if __name__ == '__main__':
    main()
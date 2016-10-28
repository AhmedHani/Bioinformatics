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

        if set(case_output) != set(k_mers):
            raise Exception("Output not matched!\nExpecting: " + str(case_output) + "\nFound: " + str(k_mers))

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for test_i in range(len(test_cases) - len(output) + 1, len(test_cases)):
        usage.start()
        case = test_cases[test_i]
        genome = case[0]
        k = case[1][0]
        d = case[1][1]
        dna = DNA(genome)
        k_mers = dna.most_frequent_missmatched_k_mer(int(k), int(d))
        usage.end()

        writer.write_data(test_i, k_mers, usage.get_execution_time(), usage.get_memory_usage())
        print("\n\nInput:\n" + genome + "\n" + str(k) + "\n" + str(d))

        print("\n\nOutput")
        print("=====")

        print('\n'.join(map(lambda v: str(v), k_mers)))

        print("\n")
        print("======")
        print("Execution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Used: " + str(usage.get_memory_usage()) + " MB")


if __name__ == '__main__':
    main()
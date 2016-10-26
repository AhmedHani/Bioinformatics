___author__ = 'Ahmed Hani Ibrahim'
from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from dna import DNA
import os
import numpy as np


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem8')
    solution_dir = os.path.join("Problems", "Problem8Solution")

    data_reader = DataReader(problem_dataset_dir)
    test_cases, output = data_reader.get_data()

    for train_i in range(0, len(output)):
        case = test_cases[train_i]
        case_output = output[train_i]
        pattern = case[0][0]
        genome = case[0][1]
        d = case[1]
        dna = DNA(genome)
        pattern_indices = dna.get_mismatched_pattern_indices(pattern, int(d))

        if case_output.sort() != pattern_indices.sort():
            raise Exception("Output not matched!\nExpecting: " + str(case_output) + "\nFound: " + str(pattern_indices))

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for test_i in range(len(test_cases) - len(output) + 1, len(test_cases)):
        usage.start()
        case = test_cases[test_i]
        pattern = case[0][0]
        genome = case[0][1]
        d = case[1]
        dna = DNA(genome)
        pattern_indices = dna.get_mismatched_pattern_indices(pattern, int(d))
        usage.end()

        writer.write_data(test_i + 1, pattern_indices, usage.get_execution_time(), usage.get_memory_usage())
        print("\n\nInput:\n" + pattern + "\n" + genome + str(d) + "\n")

        print("\n\nOutput")
        print("=====")

        print(pattern_indices)

        print("\n")
        print("======")
        print("Execution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Used: " + str(usage.get_memory_usage()) + " MB")

if __name__ == '__main__':
    main()
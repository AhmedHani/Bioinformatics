___author__ = 'Ahmed Hani Ibrahim'

from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from dna import DNA
import os


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem4')
    solution_dir = os.path.join("Problems", "Problem4Solution")

    data_reader = DataReader(problem_dataset_dir)
    test_cases, output = data_reader.get_data()

    for train_i in range(0, len(output)):
        case = test_cases[train_i]
        case_output = output[train_i]
        dna = DNA(case)
        reverse_complement = dna.reverse_complement()

        if reverse_complement != case_output:
            raise Exception("Output not matched!\nExpecting: " + str(case_output) + "\nFound: " + reverse_complement)

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for test_i in range(len(test_cases) - len(output), len(test_cases)):
        usage.start()
        case = test_cases[test_i]
        dna = DNA(case)
        reverse_complement = dna.reverse_complement()
        usage.end()

        writer.write_data(test_i + 1, reverse_complement, usage.get_execution_time(), usage.get_memory_usage())
        print("\n\nInput:\n" + case)

        print("\n\nOutput")
        print("=====")

        print(reverse_complement)

        print("\n")
        print("======")
        print("Execution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Used: " + str(usage.get_memory_usage()) + " MB")


if __name__ == '__main__':
    main()


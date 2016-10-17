___author__ = 'Ahmed Hani Ibrahim'
from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from dna import DNA
import os


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem5')
    solution_dir = os.path.join("Problems", "Problem5Solution")

    data_reader = DataReader(problem_dataset_dir)
    test_cases, output = data_reader.get_data()

    for train_i in range(0, len(output)):
        case = test_cases[train_i]
        case_output = output[train_i]
        pattern = case[0]
        genome = case[1]
        dna = DNA(genome)
        pattern_indices = dna.get_pattern_indices(pattern)

        if pattern_indices != case_output:
            raise Exception("Output not matched!\nExpecting: " + str(case_output) + "\nFound: " + pattern_indices)

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for test_i in range(len(test_cases) - len(output), len(test_cases)):
        usage.start()
        case = test_cases[test_i]
        pattern = case[0]
        genome = case[1]
        dna = DNA(genome)
        pattern_indices = dna.get_pattern_indices(pattern)
        usage.end()

        writer.write_data(test_i + 1, pattern_indices, usage.get_execution_time(), usage.get_memory_usage())
        print("\n\nInput:\n" + pattern + "\n" + genome)

        print("\n\nOutput")
        print("=====")

        print(pattern_indices)

        print("\n")
        print("======")
        print("Execution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Used: " + str(usage.get_memory_usage()) + " MB")


if __name__ == '__main__':
    main()
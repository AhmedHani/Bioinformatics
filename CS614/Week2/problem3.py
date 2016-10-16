___author__ = 'Ahmed Hani Ibrahim'

from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from dna import DNA
import os


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem3')
    solution_dir = os.path.join("Problems", "Problem3Solution")

    data_reader = DataReader(problem_dataset_dir)
    test_cases, output = data_reader.get_data()

    for train_i in range(0, len(output)):
        case = test_cases[train_i]
        case_output = output[train_i]
        dna = DNA(case[0])
        k_mers = dna.most_frequent_k_mer(int(case[1]))

        if k_mers.sort() != case_output.sort():
            raise Exception("Output not matched!\nExpecting: " + str(case_output) + "\nFound: " + str(k_mers))

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for test_i in range(len(test_cases) - len(output), len(test_cases)):
        usage.start()
        case = test_cases[test_i]
        dna = DNA(case[0])
        k_mers = dna.most_frequent_k_mer(int(case[1]))
        usage.end()

        writer.write_data(test_i, k_mers, usage.get_execution_time(), usage.get_memory_usage())
        print("\n\nInput:\n" + case[0] + "\n" + str(case[1]))

        print("\n\nOutput")
        print("=====")

        for k_mer in k_mers:
            print(k_mer)



if __name__ == '__main__':
    main()
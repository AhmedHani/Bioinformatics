___author__ = 'Ahmed Hani Ibrahim'


from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from dna import DNA
import os


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem13')
    solution_dir = os.path.join("Problems", "Problem13Solution")

    data_reader = DataReader(problem_dataset_dir)
    test_cases, output = data_reader.get_data()

    for train_i in range(0, len(output)):
        (k, genome) = test_cases[train_i]
        case_output = output[train_i]
        dna = DNA(genome)
        k_mers = dna.get_k_mers(int(k))

        if set(case_output) != set(k_mers):
            raise Exception("Output not matched!\nExpecting: " + str(case_output) + "\nFound: " + str(k_mers))

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for test_i in range(len(test_cases) - len(output), len(test_cases)):
        usage.start()
        (k, genome) = test_cases[test_i]
        dna = DNA(genome)
        k_mers = dna.get_k_mers(int(k))
        usage.end()

        writer.write_data(test_i + 1, k_mers, usage.get_execution_time(), usage.get_memory_usage())
        print("\n\nInput:\n" + k + "\n" + genome + "\n")

        print("\n\nOutput")
        print("=====")

        print(k_mers)

        print("\n")
        print("======")
        print("Execution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Used: " + str(usage.get_memory_usage()) + " MB")

if __name__ == '__main__':
    main()
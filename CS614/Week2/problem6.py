___author__ = 'Ahmed Hani Ibrahim'
from usage import Usage
from data_reader.reader import DataReader
from data_writer.writer import DataWriter
from dna import DNA
import os


def main():
    problem_dataset_dir = os.path.join('Problems', 'Problem6')
    solution_dir = os.path.join("Problems", "Problem6Solution")

    data_reader = DataReader(problem_dataset_dir)
    test_cases, output = data_reader.get_data()

    for train_i in range(0, len(output)):
        case = test_cases[train_i]
        case_output = output[train_i]
        genome = case[0]
        k = case[1][0]
        l = case[1][1][0]
        t = case[1][1][1]
        dna = DNA(genome)
        clumps_patterns = dna.get_clumps_patterns(int(k), int(t), int(l))

        if clumps_patterns.sort() != case_output.sort():
            raise Exception("Output not matched!\nExpecting: " + str(case_output) + "\nFound: " + clumps_patterns)

    print("Passed training data..")

    writer = DataWriter(solution_dir)
    usage = Usage()

    for test_i in range(len(test_cases) - len(output), len(test_cases)):
        usage.start()
        case = test_cases[test_i]
        genome = case[0]
        k = case[1][0]
        l = case[1][1][0]
        t = case[1][1][1]
        dna = DNA(genome)
        clumps_patterns = dna.get_clumps_patterns(int(k), int(t), int(l))
        usage.end()

        writer.write_data(test_i, clumps_patterns, usage.get_execution_time(), usage.get_memory_usage())
        print("\n\nInput:\n" + genome + "\n" + str(k) + " " + str(l) + " " + str(t))

        print("\n\nOutput")
        print("=====")

        for clump in clumps_patterns:
            print(clump)

        print("\n")
        print("======")
        print("Execution Time: " + str(usage.get_execution_time()) + " s")
        print("Memory Used: " + str(usage.get_memory_usage()) + " MB")




if __name__ == '__main__':
    main()
___author__ = 'Ahmed Hani Ibrahim'
import glob


class DataReader(object):
    def __init__(self, problem_dataset_dir):
        self.__problem_dataset_dir = problem_dataset_dir
        self.__test_cases = []
        self.__output = []

    def get_data(self):
        files_list = glob.glob(self.__problem_dataset_dir + "\\*.txt")
        files_list.sort()

        if "Problem3" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        dna = r.readline()
                        k_mer = r.readline()

                        self.__test_cases.append((dna.strip(), k_mer.strip()))
                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        all_k_mers = r.readlines()
                        k_mer_list = []

                        for k_mer in all_k_mers:
                            k_mer_list.append(k_mer.strip())

                        self.__output.append(k_mer_list)

        if "Problem4" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        dna = r.readline()

                        self.__test_cases.append(dna.strip())
                if file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        reverse_complement_dna = r.readline()

                        self.__output.append(reverse_complement_dna.strip())

        if "Problem5" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        pattern = r.readline()
                        genome = r.readline()

                        self.__test_cases.append((pattern.strip(), genome.strip()))
                if file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        positions = r.readline().strip()

                        self.__output.append(positions)

        if "Problem6" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        dna = r.readline()
                        k, l, t = r.readline().split(" ")

                        self.__test_cases.append((dna, (k, (l, t))))
                if file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        all_k_mers = r.readall()

                        self.__output.append(all_k_mers)

        return self.__test_cases, self.__output
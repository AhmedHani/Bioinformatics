___author__ = 'Ahmed Hani Ibrahim'
import glob


class DataReader(object):
    def __init__(self, problem_dataset_dir):
        self.__problem_dataset_dir = problem_dataset_dir
        self.__test_cases = []
        self.__output = []

        self.__blosum = {}
        self.__pam = {}

    def get_data(self):
        files_list = glob.glob(self.__problem_dataset_dir + "\\*.txt")
        files_list.sort()

        if "Problem13" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        k = r.readline().strip()
                        genome = r.readline().strip()

                        self.__test_cases.append((k, genome))

                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        k_mers = map(lambda v: v.strip(), r)

                        self.__output.append(k_mers)

        if "Problem14" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        k_mers = map(lambda v: v.strip(), r)

                        self.__test_cases.append(k_mers)

                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        adj_list = {}

                        for line in r:
                            adj_list[line.strip().split(" -> ")[0]] = line.strip().split(" -> ")[1]

                        self.__output.append(adj_list)

        if "Problem15" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        k = r.readline().strip()
                        dna = r.readline().strip()

                        self.__test_cases.append((k, dna))

                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        adj_list = {}

                        for line in r:
                            ls = []
                            for sub in line.strip().split(" -> ")[1].split(","):
                                ls.append(sub)

                            adj_list[line.strip().split(" -> ")[0]] = ls

                        self.__output.append(adj_list)

        if "Problem16" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        k_mers = map(lambda v: v.strip(), r)

                        self.__test_cases.append(k_mers)

                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        adj_list = {}

                        for line in r:
                            ls = []
                            adj_nodes = line.strip().split(" -> ")[1].split(",")

                            for sub in adj_nodes:
                                ls.append(sub)

                            adj_list[line.strip().split(" -> ")[0]] = list(set(ls))

                        self.__output.append(adj_list)

        return self.__test_cases, self.__output
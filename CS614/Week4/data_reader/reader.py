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

        if "Problem10" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        alpha_dna = r.readline().strip()
                        beta_dna = r.readline().strip()

                        self.__test_cases.append((alpha_dna, beta_dna))

                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        lcs = r.readline().strip()

                        self.__output.append(lcs)

        if "Problem8" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        pattern = r.readline().strip()
                        dna = r.readline().strip()
                        d = r.readline().strip()

                        self.__test_cases.append(((pattern, dna), d))

                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        indices = r.readline().strip().split(" ")
                        indices = map(lambda v: int(v), indices)

                        self.__output.append(indices)

        if "Problem9" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        genome = r.readline().strip()
                        k = r.readline().strip()
                        d = r.readline().strip()

                        self.__test_cases.append((genome, (k, d)))

                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        substrings = []

                        for line in r:
                            substrings.append(line.strip())

                        self.__output.append(substrings)

        return self.__test_cases, self.__output
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

        if "Problem11" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        alpha_dna = r.readline().strip()
                        beta_dna = r.readline().strip()

                        self.__test_cases.append((alpha_dna, beta_dna))

                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        score = r.readline().strip()
                        alpha_alignment = r.readline().strip()
                        beta_alignment = r.readline().strip()

                        self.__output.append((int(score), (alpha_alignment, beta_alignment)))

        if "Problem12" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        alpha_dna = r.readline().strip()
                        beta_dna = r.readline().strip()

                        self.__test_cases.append((alpha_dna, beta_dna))

                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        score = r.readline().strip()
                        alpha_alignment = r.readline().strip()
                        beta_alignment = r.readline().strip()

                        self.__output.append((int(score), (alpha_alignment, beta_alignment)))

        return self.__test_cases, self.__output
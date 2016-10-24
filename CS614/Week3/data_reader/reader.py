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

        if "Problem7" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        dna = r.readline().strip()

                        self.__test_cases.append(dna)

                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        indices = r.readline().strip().split(" ")
                        indices = map(lambda v: int(v), indices)

                        self.__output.append(indices)

        return self.__test_cases, self.__output
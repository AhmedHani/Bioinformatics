___author__ = 'Ahmed Hani Ibrahim'
import glob


class DataReader(object):
    def __init__(self, problem_dataset_dir):
        self.__problem_dataset_dir = problem_dataset_dir
        self.__training_data = []
        self.__testing_data = []

    def get_data(self):
        files_list = glob.glob(self.__problem_dataset_dir + "\\*.txt")
        files_list.sort()

        if "Problem3" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        dna = r.readline()
                        k_mer = r.readline()

                        self.__training_data.append((dna, k_mer))
                elif file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        all_k_mers = r.readall()

                        self.__testing_data.append(all_k_mers)

        if "Problem4" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        dna = r.readline()

                        self.__training_data.append(dna)
                if file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        reverse_complement_dna = r.readline()

                        self.__testing_data.append(reverse_complement_dna)

        if "Problem5" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        pattern = r.readline()
                        genome = r.readline()

                        self.__training_data.append((pattern, genome))
                if file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        positions = r.readline()
                        positions_list = positions.split(" ")

                        self.__testing_data.append(positions_list)

        if "Problem6" in self.__problem_dataset_dir:
            for file_ in files_list:
                if file_.__contains__("dataset"):
                    with open(file_, "rb") as r:
                        dna = r.readline()
                        k, l, t = r.readline().split(" ")

                        self.__training_data.append((dna, (k, (l, t))))
                if file_.__contains__("output"):
                    with open(file_, "rb") as r:
                        all_k_mers = r.readall()

                        self.__testing_data.append(all_k_mers)

        return self.__training_data, self.__testing_data







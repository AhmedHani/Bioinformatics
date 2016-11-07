___author__ = 'Ahmed Hani Ibrahim'
import glob


class DataReader(object):
    def __init__(self, problem_dataset_dir):
        self.__problem_dataset_dir = problem_dataset_dir
        self.__test_cases = []
        self.__output = []

        self.__blosum = {}
        self.__pam = {}

    def get_BLOSUM62_data(self):
        files_list = glob.glob(self.__problem_dataset_dir + "\\*.txt")
        files_list.sort()

        for file_ in files_list:
            if file_.__contains__("BLOSUM"):
                with open(file_, "rb") as reader:
                    idx = 0
                    alpha = []

                    for line in reader:
                        if idx == 0:
                            alpha = line.strip().split("  ")
                            idx += 1
                            continue

                        row = line.strip().split(" ")
                        row = filter(None, row)
                        char = row[0].strip()

                        for i in range(0, len(alpha)):
                            self.__blosum[(char, alpha[i])] = int(row[i + 1].strip())

        return self.__blosum

    def get_PAM_data(self):
        files_list = glob.glob(self.__problem_dataset_dir + "\\*.txt")
        files_list.sort()

        for file_ in files_list:
            if file_.__contains__("PAM"):
                with open(file_, "rb") as reader:
                    idx = 0
                    alpha = []

                    for line in reader:
                        if idx == 0:
                            alpha = line.strip().split("  ")
                            idx += 1
                            continue

                        row = line.strip().split(" ")
                        row = filter(None, row)
                        char = row[0].strip()

                        for i in range(0, len(alpha)):
                            self.__pam[(char, alpha[i])] = int(row[i + 1].strip())
                    break

        return self.__pam

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
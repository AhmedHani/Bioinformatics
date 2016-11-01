___author__ = 'Ahmed Hani Ibrahim'
import numpy as np


class StringsAlgorithms(object):
    def __init__(self, alpha_string="", beta_string=""):
        self.__alpha_string = alpha_string
        self.__alpha_string_length = alpha_string.__len__()
        self.__beta_string = beta_string
        self.__beta_string_length = beta_string.__len__()

    def lcs(self, algorithm='dp'):
        if algorithm is 'dp':
            return self.__lcs_dp()
        elif algorithm is 'suf':
            pass
        pass

    def alignment(self, algorithm='leve'):
        if algorithm is 'leve':
            pass
        elif algorithm is 'nwun':
            pass
        pass

    def __lcs_dp(self):
        dp_table = np.zeros((self.__alpha_string_length + 1, self.__beta_string_length + 1))

        for i in range(1, self.__alpha_string_length + 1):
            for j in range(1, self.__beta_string_length + 1):
                if self.__alpha_string[i - 1] == self.__beta_string[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1] + 1
                else:
                    dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

        #print(dp_table[self.__alpha_string_length][self.__beta_string_length])

        lcs_string = ""
        alpha_ptr = self.__alpha_string_length
        beta_ptr = self.__beta_string_length

        while alpha_ptr != 0 and beta_ptr != 0:
            if dp_table[alpha_ptr][beta_ptr] == dp_table[alpha_ptr][beta_ptr - 1]:
                beta_ptr -= 1
            elif dp_table[alpha_ptr][beta_ptr] == dp_table[alpha_ptr - 1][beta_ptr]:
                alpha_ptr -= 1
            else:
                lcs_string += self.__alpha_string[alpha_ptr - 1]
                alpha_ptr -= 1
                beta_ptr -= 1

        return lcs_string[::-1]

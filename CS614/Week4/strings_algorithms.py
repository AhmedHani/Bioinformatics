___author__ = 'Ahmed Hani Ibrahim'
import numpy as np
import copy as cp
from numpy import unravel_index


class StringsAlgorithms(object):
    def __init__(self, alpha_string="", beta_string=""):
        self.__alpha_string = alpha_string
        self.__alpha_string_length = alpha_string.__len__()
        self.__beta_string = beta_string
        self.__beta_string_length = beta_string.__len__()

    def lcs(self, algorithm='dp'):
        return self.__lcs_dp() if algorithm == 'dp' else self.__lcs_dp()

    def alignment(self, _type='global', scoring_matrix=dict):
        if _type is 'local':
            return self.__smith_waterman(scoring_matrix)
        elif _type is 'global':
            return self.__needleman_wunsch(scoring_matrix)

    def __lcs_dp(self):
        dp_table = np.zeros((self.__alpha_string_length + 1, self.__beta_string_length + 1))

        for i in range(1, self.__alpha_string_length + 1):
            for j in range(1, self.__beta_string_length + 1):
                if self.__alpha_string[i - 1] == self.__beta_string[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1] + 1
                else:
                    dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

        # print(dp_table[self.__alpha_string_length][self.__beta_string_length])

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

    def __needleman_wunsch(self, scoring_matrix):
        gab_penalty = -5
        dp_table = np.zeros((self.__alpha_string_length + 1, self.__beta_string_length + 1))

        for i in range(0, self.__alpha_string_length + 1):
            dp_table[i][0] = gab_penalty * i

        for j in range(0, self.__beta_string_length + 1):
            dp_table[0][j] = gab_penalty * j

        for i in range(0, self.__alpha_string_length + 1):
            for j in range(0, self.__beta_string_length + 1):
                dp_table[i][j] = max(
                    dp_table[i - 1][j - 1] + scoring_matrix[(self.__alpha_string[i - 1], self.__beta_string[j - 1])],
                    dp_table[i - 1][j] + gab_penalty,
                    dp_table[i][j - 1] + gab_penalty
                )

        alpha_alignment = ""
        beta_alignment = ""
        alpha_ptr = self.__alpha_string_length
        beta_ptr = self.__beta_string_length

        while alpha_ptr > 0 and beta_ptr > 0:
            if dp_table[alpha_ptr][beta_ptr] == dp_table[alpha_ptr - 1][beta_ptr - 1] + scoring_matrix[(self.__alpha_string[alpha_ptr - 1], self.__beta_string[beta_ptr - 1])]:
                alpha_alignment += self.__alpha_string[alpha_ptr - 1]
                beta_alignment += self.__beta_string[beta_ptr - 1]
                alpha_ptr -= 1
                beta_ptr -= 1
            elif dp_table[alpha_ptr][beta_ptr] == dp_table[alpha_ptr - 1][beta_ptr] + gab_penalty:
                alpha_alignment += self.__alpha_string[alpha_ptr - 1]
                beta_alignment += "-"
                alpha_ptr -= 1
            elif dp_table[alpha_ptr][beta_ptr] == dp_table[alpha_ptr][beta_ptr - 1] + gab_penalty:
                alpha_alignment += "-"
                beta_alignment += self.__beta_string[beta_ptr - 1]
                beta_ptr -= 1

        while alpha_ptr > 0:
            alpha_alignment += self.__alpha_string[alpha_ptr - 1]
            beta_alignment += "-"
            alpha_ptr -= 1

        while beta_ptr > 0:
            alpha_alignment += "-"
            beta_alignment += self.__beta_string[beta_ptr - 1]
            beta_ptr -= 1

        alpha_alignment = alpha_alignment[::-1]
        beta_alignment = beta_alignment[::-1]

        score = 0

        for i in range(0, len(alpha_alignment)):
            if alpha_alignment[i] == beta_alignment[i]:
                score += scoring_matrix[(alpha_alignment[i], beta_alignment[i])]
            elif alpha_alignment[i] != beta_alignment[i] and alpha_alignment[i] != "-" and beta_alignment[i] != "-":
                score += scoring_matrix[(alpha_alignment[i], beta_alignment[i])]
            elif alpha_alignment[i] == "-":
                score += gab_penalty
            elif beta_alignment[i] == "-":
                score += gab_penalty

        all_res = (score, (alpha_alignment, beta_alignment))

        return all_res

    def __smith_waterman(self, scoring_matrix):
        gab_penalty = -5
        dp_table = np.zeros((self.__alpha_string_length + 1, self.__beta_string_length + 1))
        local_alignment_ending_pointer = cp.copy(dp_table)

        for i in range(0, self.__alpha_string_length + 1):
            for j in range(0, self.__beta_string_length + 1):
                end = 0
                diagonal = dp_table[i - 1][j - 1] + scoring_matrix[(self.__alpha_string[i - 1], self.__beta_string[j - 1])]
                up = dp_table[i][j - 1] + gab_penalty
                left = dp_table[i - 1][j] + gab_penalty
                all_ = [left, up, diagonal, end]
                dp_table[i][j] = max(all_)
                local_alignment_ending_pointer[i][j] = all_.index(dp_table[i][j])

        alpha_ptr, beta_ptr = unravel_index(dp_table.argmax(), dp_table.shape)
        maximum_score = int(dp_table[alpha_ptr][beta_ptr])

        alpha_alignment = ""
        beta_alignment = ""

        while local_alignment_ending_pointer[alpha_ptr][beta_ptr] != 3 and alpha_ptr > 0 and beta_ptr > 0:
            if local_alignment_ending_pointer[alpha_ptr][beta_ptr] == 2:
                alpha_alignment += self.__alpha_string[alpha_ptr - 1]
                beta_alignment += self.__beta_string[beta_ptr - 1]
                alpha_ptr -= 1
                beta_ptr -= 1
            if local_alignment_ending_pointer[alpha_ptr][beta_ptr] == 1:
                beta_alignment += self.__beta_string[beta_ptr - 1]
                alpha_alignment += "-"
                beta_ptr -= 1
            if local_alignment_ending_pointer[alpha_ptr][beta_ptr] == 0:
                alpha_alignment += self.__alpha_string[alpha_ptr - 1]
                beta_alignment += "-"
                alpha_ptr -= 1

        alpha_alignment = alpha_alignment[::-1]
        beta_alignment = beta_alignment[::-1]

        all_res = (maximum_score, (alpha_alignment, beta_alignment))

        return all_res




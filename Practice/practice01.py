from collections import Counter
from string import ascii_uppercase


# ["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]

# ["김비바A", "김비바B", "이비바A", "김토스A", "이비바B", "김비바C"]


def solution(name_list):
    answer = []

    temp_a = []
    temp_b = []
    temp_c = []
    alpha_list = list(ascii_uppercase)

    result = Counter(name_list)

    for keys, values in result.items():
        temp_a.append(keys)
        temp_b.append(values)
        temp_c.append(0)

    for name in name_list:

        for dupl_name in temp_a:

            if name == dupl_name:

                answer.append(name + alpha_list[temp_c[temp_a.index(name)]])
                temp_c[temp_a.index(name)] += 1
                break
            else:
                print(temp_a.index(name))
                answer.append(name + alpha_list[temp_c[temp_a.index(name)]])

                temp_c[temp_a.index(name)] += 1
                break

    return answer


print(solution(["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]))

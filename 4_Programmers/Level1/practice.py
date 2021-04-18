n = 123854

# b = ''.join(sorted(str(n), reverse=True))

# print(b)


def solution(n):
    answer = ''.join(sorted(str(n), reverse=True))
    return answer


print(solution(n))

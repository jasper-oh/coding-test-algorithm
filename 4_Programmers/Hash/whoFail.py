import collections

# lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
# print(collections.Counter(lst))

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

# print(collections.Counter(participant) - collections.Counter(completion))


def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}

    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)

    answer = dic[temp]
    return answer

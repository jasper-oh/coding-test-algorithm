#   n = 행의 갯수 / m = 열의 갯수
#   가장 높은 숫자를 뽑아야 한다.

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)


for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value,a)
    result = max(result, min_value)
print(result)
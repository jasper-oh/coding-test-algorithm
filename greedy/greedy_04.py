# 1. N 에서 1을 뺀다
# 2. N 을 K로 나눈다
# 최소 과정으로 1이 될때까지 1번 2번 과정을 반복한다
# 최소 과정의 숫자는?

n, k = map(int, input().split())

result = 0

while True:
    if k == 1:
        result += n
        break
    target = (n//k) * k
    result += (n-target)
    n = target

    if n < k:
        break
    result += 1
    n //= k
if k == 1:
    result = n
else:
    result += (n-1)
print(result)

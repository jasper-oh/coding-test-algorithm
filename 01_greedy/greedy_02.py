# n = 입력받는 배열 data 의 길이,크기
# m = 배열을 총 더하는 횟수
# k = 배열의 원소를 중복해서 더할수 있는 수 result = 가장 큰수를 만들어라

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1

count = int(m / (k+1)) * k
count += m % (k+1)

result += count * first
result += (m-count) * second


print(result)

# BUT what if one's added number, then shoudn't be added twice..?

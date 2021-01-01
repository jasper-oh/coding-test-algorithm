x = int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array)

for i in range(2, x):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[x-1])

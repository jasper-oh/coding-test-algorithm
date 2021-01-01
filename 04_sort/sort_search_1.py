# n = int(input())
# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] = 1

# m = int(input())
# request = list(map(int, input().split()))

# for i in request:
#     if array[i] == 1:
#         print('yes', end=" ")
#     else:
#         print('no', end=" ")

array = [2, 3, 4, 5, 6]
start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start+end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

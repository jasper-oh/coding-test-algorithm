n, m = list(map(int, input().split()))

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end)//2
    for x in array:
        if x > mid:
            total += x - mid
    # for 구문이 끝나고 난후 들어감
    if total < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)

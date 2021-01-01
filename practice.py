def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
result = binary_search_2(array, target, 0, n-1)
if result == None:
    print("There's no element")
else:
    print(result+1)

# 반복문을 이용한 이진 탐색


def binary_search_2(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == traget:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

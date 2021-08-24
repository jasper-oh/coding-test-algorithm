#  이진 탐색
# 코딩 테스트 문제에도 나옴.


# start 와 end 는 어떻게 사용되는 놈이지?
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())

array = list(map(int, input().split()))
array.sort()

m = int(input())
request = list(map(int, input().split()))

for i in request:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=" ")
    else:
        print('no', end=" ")

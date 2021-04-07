

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
#  their are array !!

for i in range(len(array)):

    min_index = i

    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # SWAP
    array[i], array[min_index] = array[min_index], array[i]

print(array)


# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j-1]:
#             array[j],array[j-1] =array[j-1],array[j]
#         else:
#             break
# print(array)


# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[right] = array[right], array[left]
#     quick_sort(array, start, right-1)
#     quick_sort(array, right+1, end)


# quick_sort(array, 0, len(array)-1)
# print(array)


# array = [2, 3, 1]
# for i in range(5):
#     k, m, n = list(map(int, input().split()))

# while k == 1:
#     print("k is 1")
#     while m == 2:
#         q += 1
#         break
#     while n == 3:
#         w += 1
#         break
#     if n != 3:
#         e += 1
#         break
#     else:
#         r += 1n
#         break


array = "FUCK"
code = []
for i in array:
    code.append(ord(i))
print(code)

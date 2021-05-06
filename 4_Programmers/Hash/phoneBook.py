
# phone_book = ["119", "97674223", "1195524421"]
phone_book = ["123", "456", "789"]
# phone_book = ["119", "97674223", "1195524421"]


# def solution(phone_book):
#     for phone in phone_book:
#         temp = ''
#
#
#   for num in phone:
#             temp += num
#             if temp in phone_book and temp != phone:
#                 return False
#     return True


# print(solution(phone_book))

#  startswith 함수를 사용해서 시작되는 값들을 지정 할 수 있다!

def solution(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

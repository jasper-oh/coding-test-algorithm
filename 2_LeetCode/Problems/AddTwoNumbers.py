# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):

        result = ListNode(0)

        result_tail = result

        carry = 0

        while l1 or l2 or carry:

            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            #  진행을 하면서 할것들
            carry, out = divmod(val1 + val2 + carry, 10)

            #  진행을 여기서 부터 한다
            result_tail.next = ListNode(out)

            result.next = result_tail.next

            # 여기 까지 진행 할것이다.
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l1 else None)

        return result

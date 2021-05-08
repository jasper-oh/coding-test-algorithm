class NodeList:
    def __init__(self, var=0, next=None):
        self.var = var
        self.next = next


# l1 = NodeList()
# l2 = NodeList()

l1 = [2, 4, 3]
l2 = [5, 6, 4]


class Solution:
    def printThings(self, l1: NodeList, l2: NodeList) -> NodeList:
        l3 = l1 + l2
        return l3


s1 = Solution()

print(s1.printThings)

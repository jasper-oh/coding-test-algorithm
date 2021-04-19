# answerF = ["119", "97674223", "1195524421"]

lst1 = [1, 2, 3]
lst2 = ["one", "two", "three"]
cLst = set(zip(lst1, lst2))


print(cLst)

print(type(cLst))

a = [(1, 2), (2, 3), (3, 4)]
b = {1: "one", 2: "two", 3: "three"}
c = {(1, "one"), (2, "two"), (3, "three")}


lst2 = ["one", "two", "three"]
lst4 = {(), (), ()}
# lst4 = [(1, "one"), (2, "two"), (3, "three")]
# lst5 = ((1, "one"), (2, "two"), (3, "three"))
# print(type(lst3))
# print(type(lst4))

# print(type(cLst))

cLst = set(cLst)
print(type(c))
# print(type(lst1))
# print(type(lst4))
# print(type(lst3))
# print(type(cLst))
# print(cLst)


# for p1, p2 in zip(answerF, answerF[1:]):
#     if p2.startswith(p1):
#         print(False)

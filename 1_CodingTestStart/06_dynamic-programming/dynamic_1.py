# Dynamic Algorithms

# Understanding Basic of Dynamic Algorithms
x = int(input())

d = [0] * 100
for i in range(2, x+1):
    d[i] = d[i-1] + 1
    print(i)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
        print("2로 나뉨")
    else:
        print("2 x")
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
        print("3으로 나뉨")
    else:
        print("3 x")
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
        print("5로 나뉨")
    else:
        print("5 x")
print(d[x])

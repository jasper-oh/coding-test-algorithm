# if Number was input, then 00h 00m 00s to Nh 59m 59m
# how many '3' during those times ?

h = int(input())
count = 0

for h in range(h+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1
print(count)

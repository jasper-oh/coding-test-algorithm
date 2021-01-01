h = int(input())

count = 0

for hour in range(h+1):
    for minute in range(60):
        for sec in range(60):
            if '3' in str(hour) + str(minute) + str(sec):
                count += 1

print(count)

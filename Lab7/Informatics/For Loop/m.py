n = int(input())
cnt = 0 #we count number of zeros among given numbers

for i in range(n):
    number = int(input())
    if (number == 0):
        cnt += 1

print(cnt)
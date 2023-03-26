n = int(input())
arr = input().split()
cnt = 0

for num in arr:
    if int(num) > 0:
        cnt += 1

print(cnt)
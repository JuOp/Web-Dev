n = int(input())
arr = input().split()
prev = arr[0]
cur = arr[1]
cnt = 0

for i in range(2, n):
    next = arr[i]
    if int(cur) > int(prev) and int(cur) > int(next):
        cnt += 1
    prev = cur
    cur = next

print(cnt)
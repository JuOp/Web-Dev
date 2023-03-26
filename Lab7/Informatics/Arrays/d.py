n = int(input())
arr = input().split()
prev = arr[0]
cnt = 0

for i in range(1, len(arr)):
    if int(arr[i]) > int(prev):
        cnt += 1
    prev = arr[i]

print(cnt)





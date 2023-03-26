n = int(input())
arr = input().split()
prev = arr[0]


for i in range(1, n):
    current = arr[i]
    if (int(current) > 0 and int(prev) > 0) or (int(current) < 0 and int(prev) < 0):
        print("YES")
        quit()
    prev = current

print("NO")
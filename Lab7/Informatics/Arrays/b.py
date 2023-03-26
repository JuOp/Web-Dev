size = int(input())
arr = input().split()

for number in arr:
    if int(number) % 2 == 0:
        print(number, end=' ')
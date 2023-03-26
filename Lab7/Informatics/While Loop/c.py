from re import I


n = int(input())

i, div = 1, 1

while i <= n:
    if (i % div == 0):
        print(i, end=' ')
        div = i
    i += 1
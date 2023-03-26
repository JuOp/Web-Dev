n = int(input())

while n % 2 == 0:
    n//=2

answer = "YES" if n == 1 else "NO"

print(answer)
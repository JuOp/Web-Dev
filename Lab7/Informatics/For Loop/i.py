number = int(input())
cnt = 0 #we count divisors of the given number

for i in range (1, number+1):
    if number % i == 0:
        cnt+=1

print(cnt)
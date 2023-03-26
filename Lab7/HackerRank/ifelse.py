n = int(input())

n_is = "Weird" if (n % 2 == 1 and n < 21) or (n % 2 == 0 and n in range(6, 21)) else "Not Weird"

print(n_is)
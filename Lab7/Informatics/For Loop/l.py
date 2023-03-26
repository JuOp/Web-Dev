number = input()
sum = 0
to_convert = str(reversed(number))

for i in range(len(to_convert)):
    sum += int(to_convert[i])**i

print(sum)
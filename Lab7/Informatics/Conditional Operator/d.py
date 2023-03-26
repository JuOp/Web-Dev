from signal import signal


num = int(input())
global sign

if num == 0:
    sign = 0
elif num > 0:
    sign = 1
else:
    sign = -1

print(sign)
MRAR_LENGTH = 109 #const
velocity = int(input())
time = int(input())

global location

if velocity > 0:
    location = (velocity*time)%MRAR_LENGTH
elif velocity < 0:
    location = (MRAR_LENGTH + (velocity*time)%MRAR_LENGTH)%MRAR_LENGTH

print(location)
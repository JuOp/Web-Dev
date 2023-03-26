def xor(a, b):
    return 0 if a == b else 1

a, b = map(bool, input().split())

print(xor(a, b))
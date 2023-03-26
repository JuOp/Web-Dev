def left2(str):
    return str if len(str) <= 2 else str[2:] + str[:2]
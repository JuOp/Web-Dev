def front_back(str):
    return str if len(str) <= 1 else str[len(str)-1] + str[1:len(str)-1] + str[0]
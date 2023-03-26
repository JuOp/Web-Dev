def string_splosion(str):
    answer = ''
    for i in range(len(str)):
        answer += str[:i+1]
    return answer
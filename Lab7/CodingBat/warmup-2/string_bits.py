def string_bits(str):
  answer = ""
  for i in range(len(str)):
    if i % 2 == 0:
      answer += str[i]
  return answer

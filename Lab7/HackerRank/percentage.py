n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
sum = sum(student_marks[query_name])
length = len(student_marks[query_name])
print(sum/length)


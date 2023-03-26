n = int(input())
scores = (int(score) for score in input().split())

i = scores.index(max(scores))

scores[i] = -111

print(max(scores))
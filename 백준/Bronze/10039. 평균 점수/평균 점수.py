scores = []
for i in range(5):
    score = int(input())
    if score < 40:
        scores.append(40)
        continue
    scores.append(score)

print(sum(scores)//5)
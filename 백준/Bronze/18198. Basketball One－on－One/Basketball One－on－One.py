x = list(input())
i = 0 
score_a = 0
score_b = 0
f = 0
while True:
    # print(x[i])
    if x[i] == 'A':
        score_a += int(x[i+1])
    elif x[i] == 'B':
        score_b += int(x[i+1])
    # print(f"score_a = {score_a}, score_b = {score_b}")
    if score_a == 10 and score_b == 10:
        i += 2
        while True:
            if x[i] == 'A':
                score_a += int(x[i+1])
            elif x[i] == 'B':
                score_b += int(x[i+1])
            if score_a >= score_b + 2 or score_b >= score_a + 2:
                f = 1
                break
            i += 2
    if f == 1:
        break
    if score_a == 11 or score_b == 11:
        break
    if i == len(x) - 2:
        break
    i += 2

if score_a > score_b:
    print("A")
elif score_b > score_a:
    print("B")
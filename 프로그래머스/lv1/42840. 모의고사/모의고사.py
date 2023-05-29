def solution(answers):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(answers)):
        if i%10 == 0 and answers[i] == 3:
            cnt3 += 1
        if i%10 == 1 and answers[i] == 3:
            cnt3 += 1
        if i%10 == 2 and answers[i] == 1:
            cnt3 += 1
        if i%10 == 3 and answers[i] == 1:
            cnt3 += 1
        if i%10 == 4 and answers[i] == 2:
            cnt3 += 1
        if i%10 == 5 and answers[i] == 2:
            cnt3 += 1
        if i%10 == 6 and answers[i] == 4:
            cnt3 += 1
        if i%10 == 7 and answers[i] == 4:
            cnt3 += 1
        if i%10 == 8 and answers[i] == 5:
            cnt3 += 1
        if i%10 == 9 and answers[i] == 5:
            cnt3 += 1

        if i%2 == 0 and answers[i] == 2:
            cnt2 += 1
        if i%8 == 1 and answers[i] == 1:
            cnt2 += 1
        if i%8 == 3 and answers[i] == 3:
            cnt2 += 1
        if i%8 == 5 and answers[i] == 4:
            cnt2 += 1
        if i%8 == 7 and answers[i] == 5:
            cnt2 += 1    

        if i%5 == 0 and answers[i] == 1:
            cnt1 += 1
        if i%5 == 1 and answers[i] == 2:
            cnt1 += 1
        if i%5 == 2 and answers[i] == 3:
            cnt1 += 1
        if i%5 == 3 and answers[i] == 4:
            cnt1 += 1
        if i%5 == 4 and answers[i] == 5:
            cnt1 += 1
    max_cnt = max(cnt1, cnt2, cnt3)
    
    s = [(cnt1, 1), (cnt2, 2), (cnt3, 3)]
    answer = []
    for i in range(len(s)):
        if s[i][0] == max_cnt:
            answer.append(s[i][1])
    
    return answer
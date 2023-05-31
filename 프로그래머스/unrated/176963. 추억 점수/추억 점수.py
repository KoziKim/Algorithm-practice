def solution(name, yearning, photo):
    hash = {}
    for i in range(len(name)):
        hash[name[i]] = yearning[i]
    answer = []
    for i in range(len(photo)):
        part_sum = 0
        for j in range(len(photo[i])):
            if photo[i][j] in hash:
                part_sum += hash[photo[i][j]]
        answer.append(part_sum)
    return answer
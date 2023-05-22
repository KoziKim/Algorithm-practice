from collections import deque
def solution(babbling):
    speak = [["a","y","a"], ["y","e"], ["w","o","o"], ["m","a"]]
    answer = 0
    len_ = len(babbling)
    for i in range(len_):
        compare = list(babbling[i])
        while True:
            if len(compare) == 0:
                answer += 1
                break
            if len(compare) < 2:
                break
            flag = 0
            for j in range(4):
                print("spe", speak[j])
                print("comp", compare[-3:])
                if len(compare) < 2 or not compare:
                    break
                if len(compare) >= 3 and speak[j] == compare[-3:]:
                    if len(compare) >= 6 and speak[j] == compare[-6:-3]:
                        while len(compare) > 1:
                            compare.pop()
                        break
                    compare.pop()
                    compare.pop()
                    compare.pop()
                elif len(compare) >= 2 and speak[j] == compare[-2:]:
                    if len(compare) >= 4 and speak[j] == compare[-4:-2]:
                        while len(compare) > 1:
                            compare.pop()
                        break
                    compare.pop()
                    compare.pop()
                else:
                    flag += 1
                if flag == 4:
                    while len(compare) > 1:
                        compare.pop()
                    break
    return answer
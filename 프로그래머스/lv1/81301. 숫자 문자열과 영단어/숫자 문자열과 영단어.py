def solution(s):
#     s == one4seveneight
    name = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    eng = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    i = 0
    ans = []
    while i < len(s):
        skip = 0
        if s[i].isdigit():
            ans.append(s[i])
            skip = 1
        else:
            for j in range(len(name)):
                if i+len(name[j]) <= len(s):
                    if s[i:i+len(name[j])] == name[j]:
                        ans.append(eng[name[j]])
                        skip = len(name[j])
                        break
        i += skip
    answer = int(''.join(ans))
    return answer
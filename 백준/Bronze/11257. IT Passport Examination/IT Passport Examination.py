n = int(input())

for i in range(n):
    candi, strg, it, tech = map(int, input().split())
    if (strg + it + tech) >= 55 and strg >= 35*0.3 and it >= 25*0.3 and tech >= 40*0.3:
        print(candi, strg+it+tech, "PASS")
    else:
        print(candi, strg+it+tech, "FAIL")
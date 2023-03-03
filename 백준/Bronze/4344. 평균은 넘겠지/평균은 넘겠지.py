N = int(input())
S = 0
over = int()

for i in range(0, N):
    A = input().split()
    sn = int(A[0])
    for j in range(1, sn + 1):
        S = S + int(A[j])
        if j == sn:
            for k in range(1, sn + 1):
                if float(A[k]) > S/sn:
                    over = over + 1
                if k == sn:
                    tmp = over/sn*100
                    ans = "%0.3f" % tmp
                    real = str(ans) + "%"
                    print(real)
                    over = 0 
            S = 0
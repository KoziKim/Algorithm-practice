import sys

input = sys.stdin.readline

N = int(input())

pos = [0] * N
flag_1 = [False] * N
flag_2 = [False] * (2*N-1) 
flag_3 = [False] * (2*N-1)
cnt = 0

def set(i):
    global cnt
    for j in range(N):
        if (not flag_1[j] and not flag_2[i + j] and not flag_3[i - j + N-1]):
            pos[i] = j
            if i == N-1:
                cnt += 1
            else:
                flag_1[j] = flag_2[i+j] = flag_3[i-j+N-1] = True
                set(i + 1)
                flag_1[j] = flag_2[i+j] = flag_3[i-j+N-1] = False

set(0)
print(cnt)
import sys
from heapq import heappush as hpush, heappop as hpop
input = sys.stdin.readline

N = int(input())

leftheap = []
rightheap = []
ans = []

for i in range(N):
    num = int(input())
    # leftheap, rightheap에 순서대로 heappush를 해준다.
    if i%2 == 0:
        hpush(leftheap, (-num, num))
    else:
        hpush(rightheap, (num, num))
    # leftheap에 중간값보다 작은 값이 들어가야하기 때문에 
    # leftheap값이 rightheap값보다 크면 서로 바꿔준다.
    if rightheap and leftheap[0][1] > rightheap[0][1]:
        small = hpop(rightheap)[1] #rightheap[0][1] 
        big = hpop(leftheap)[1] #leftheap[0][1]
        hpush(leftheap, (-small, small))
        hpush(rightheap, (big, big))
    ans.append(leftheap[0][1]) # leftheap 최솟값이 중간값이다.(음수기 때문)

for _ in ans:
    print(_)

# 7
# 1
# 5
# 2
# 10
# -99
# 7
# 5
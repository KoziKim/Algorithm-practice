n, k = map(int, input().split())
a = list(map(int, input().split()))
check = 0
tap = [0] * n
cnt = 0
comp = 101
_now = 0
far = 0
if k <= n:
    print(0)
    exit()

for i in range(k):
    if a[i] in tap: # 이미 꽂혀 있다면, 넘긴다.
        pass
    elif 0 in tap: # 여유 자리 있을 때,
        tap[tap.index(0)] = a[i] # 여유 자리에 넣는다.
    else: # 여유 자리 없다면,
        for j in tap: # 멀티탭에 꽂혀있는 것들 중
            if j not in a[_now:]: # 뒤에 다시 안나오면
                tmp = j # 뽑을 값으로 선택
                break
            elif a[_now:].index(j) > far: # 나중에 나오는 값 인덱스 찾기
                far = a[_now:].index(j) # 멀리 있는 인덱스로 갱신
                tmp = j # 뽑을 값 갱신 (더 나중에 나오는 걸 뽑아야 효율적이니까)
        tap[tap.index(tmp)] = a[i] # 뽑고 끼운다.
        far = 0
        cnt += 1
    _now += 1

print(cnt)
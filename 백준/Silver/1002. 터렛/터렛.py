t = int(input())
for i in range(t):
    x, y, r1, a, b, r2 = map(int, input().split())
    length = ((x-a)**2 + (y-b)**2)**(1/2) # 두 점 간의 거리
    if x == a and y == b: # 두 점이 일치
        if r1 == r2:
            print(-1)
        elif r1 != r2:
            print(0)
    else: # 두 점이 일치하지 않을 때,
        if r1 > r2:
            if r1 > length + r2: # r1이 (r2 + 점 간의 거리)보다 큼. 0
                print(0)
            elif r1 < length + r2 and r1 > length - r2: # r1이 (r2 + 점 간의 거리)보다 작고 (r2 - 점 간의 거리)보다 큼.
                print(2)
            elif r1 == length + r2: # r1이 (r2 + 점 간의 거리)랑 같음. 한점
                print(1)
            elif r1 < length - r2: #r1이 거리 - r2 보다 작음. 안만남
                print(0)
            elif r1 == length - r2: # r1이 (r2 - 점 간의 거리)랑 같음. 한점
                print(1)
        elif r2 > r1:
            if r2 > length + r1: # r2가
                print(0)
            elif r2 < length + r1 and r2 > length - r1: # r2가
                print(2)
            elif r2 == length + r1: # r2가
                print(1)
            elif r2 < length - r1: #r2가. 안만남
                print(0)
            elif r2 == length - r1: # r1이 (r2 - 점 간의 거리)랑 같음. 한점
                print(1)
        else: # r1 == r2
            if length == r1 + r2:
                print(1)
            elif length > r1 + r2:
                print(0)
            elif length < r1 + r2:
                print(2)
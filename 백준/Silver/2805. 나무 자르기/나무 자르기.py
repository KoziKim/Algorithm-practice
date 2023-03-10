N, M = map(int, input().split())

q = []
treeH = list(map(int, input().split()))
left, right = 1, max(treeH)  # 이진 탐색을 위한 변수 설정

while left <= right:  # 이진 탐색 시작
    mid = (left + right) // 2
    total = 0
    for h in treeH:
        if h - mid > 0:
            total += h - mid
    if total < M:
        right = mid - 1
    else:
        left = mid + 1

print(right)
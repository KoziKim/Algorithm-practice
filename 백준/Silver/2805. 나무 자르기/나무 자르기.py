def cut(trees, mid):
    # mid 길이로 나무들을 잘랐을 때 얻을 수 있는 나무의 길이 합을 계산
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    return total

def binary_search(trees, target):
    left, right = 1, max(trees) # left는 최소 1, right은 나무 중 가장 긴 길이로 설정
    result = 0

    while left <= right:
        mid = (left + right) // 2
        total = cut(trees, mid)

        if total >= target: # 더 많은 길이를 얻을 수 있는 경우
            result = mid
            left = mid + 1
        else: # 더 적은 길이를 얻을 수 있는 경우
            right = mid - 1

    return result

n, target = map(int, input().split())
trees = list(map(int, input().split()))

print(binary_search(trees, target))

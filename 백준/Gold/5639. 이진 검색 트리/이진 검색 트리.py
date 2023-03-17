import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
nums = []
while True:
    try:
        num = int(input())
        nums.append(num)
    except:
        break

def postorder(root, end): #0, 8
    if root > end:
        return
    mid = end + 1 #9
    for i in range(root + 1, end + 1): #1, 9 (1~8)
        if nums[i] > nums[root]: # i번째 수가 루트 노드보다 더 크면,
            mid = i # 큰 수 해당하는 인덱스 mid에 넣음
            break
    postorder(root + 1, mid - 1) # 왼쪽 (작은 수)
    postorder(mid, end) # 오른쪽 (큰 수)
    print(nums[root]) # 루트

postorder(0, len(nums)-1)
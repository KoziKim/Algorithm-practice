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
    mid = end + 1 #9 #6
    for i in range(root + 1, end + 1): #1, 9 #1, 6
        if nums[i] > nums[root]: #i번째 수가 루트 노드보다 더 크면,
            mid = i
            break
    postorder(root + 1, mid - 1) #1, 5
    postorder(mid, end) #6, 8
    print(nums[root])

postorder(0, len(nums)-1)
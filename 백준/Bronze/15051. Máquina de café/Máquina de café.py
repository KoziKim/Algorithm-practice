a1 = int(input())  # 1층의 직원 수 입력
a2 = int(input())  # 2층의 직원 수 입력
a3 = int(input())  # 3층의 직원 수 입력

# 각 층별로 커피를 마실 때 필요한 시간 계산
time_1 = 2 * a2 + 4 * a3
time_2 = 2 * a1 + 2 * a3
time_3 = 4 * a1 + 2 * a2

# 최소 시간을 선택하여 출력
print(min(time_1, time_2, time_3))
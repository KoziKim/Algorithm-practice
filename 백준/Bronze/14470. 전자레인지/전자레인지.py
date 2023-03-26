a = int(input())
end = int(input())
time_f1 = int(input())
time_f_to_nf = int(input())
time_nf1 = int(input())
ans = 0
while a < 0:
    a += 1
    ans += time_f1
if a == 0:
    ans += time_f_to_nf
while a < end:
    a += 1
    ans += time_nf1
print(ans)
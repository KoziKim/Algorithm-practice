mhsj = []
yj = []
for i in range(4):
    mhsj.append(int(input()))
for i in range(2):
    yj.append(int(input()))
mhsj.sort()
yj.sort()

print(sum(mhsj[1:])+yj[1])
fish = []
for i in range(4):
    fish.append(int(input()))

if fish[0] == fish[1] == fish[2] == fish[3]:
    print("Fish At Constant Depth")
elif fish[0] < fish[1] < fish[2] < fish[3]:
    print("Fish Rising")
elif fish[0] > fish[1] > fish[2] > fish[3]:
    print("Fish Diving")
else:
    print("No Fish")
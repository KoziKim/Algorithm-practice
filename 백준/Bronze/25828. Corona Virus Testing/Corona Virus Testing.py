num_group, people_in, positive_g = map(int, input().split())

indi = num_group * people_in
test_g = num_group + positive_g * people_in
if indi < test_g:
    print(1)
elif indi > test_g:
    print(2)
else:
    print(0)
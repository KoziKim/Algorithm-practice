todayT, todayW = map(int, input().split())
T, W = map(int, input().split())

if T < 0 and W >= 10:
    print("A storm warning for tomorrow! Be careful and stay home if possible!")
elif T < todayT:
    print("MCHS warns! Low temperature is expected tomorrow.")
elif W > todayW:
    print("MCHS warns! Strong wind is expected tomorrow.")
else:
    print("No message")
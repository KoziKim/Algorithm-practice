s_limit = int(input())
myspeed = int(input())

over = myspeed - s_limit

if myspeed <= s_limit:
    print("Congratulations, you are within the speed limit!")
elif over <= 20:
    print(f"You are speeding and your fine is $100.")
elif 21 <= over <= 30:
    print(f"You are speeding and your fine is $270.")
elif 31 <= over:
    print(f"You are speeding and your fine is $500.")
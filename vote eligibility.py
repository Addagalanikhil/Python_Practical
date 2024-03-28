age = int(input())

if age >= 18:
    print("You are eligible to vote")
elif age < 0:
    print("invalid input")
else:
    vote = 18 - age
    print(f"You are eligible after {vote} years")
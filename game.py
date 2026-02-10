import random as rand


random_number = rand.randint(0,10)
print("=======Mini-Game=========\n")
print("Guess an Number between (1-10)\n")
guess_num :int =int(input("Enter A Number:"))

if guess_num == random_number:
    print(f"Yahooo Mn Jeet Gya {random_number}")
    # break
else:
    print(f"Try Again , {random_number}")


import random as rand



print("============Mini-Cricket-match================\n")
print("Rules: Choose a number 1-6. If your number matches computer's number, you're OUT!")


user_score = 0
computer_score = 0
turns = 6


print("\nYour Batting Turn:")

for i in range(turns):
    user = int(input(f"Bowl {i+1}: Enter The Number(1-6)"))
    comput = rand.randint(1,6)
    print(f"Computer bowled: {comput}")


    if user == comput:
        print("You are Out!")
        break
    else:
        user_score += user
        print(f"Run Scored {user_score}")
print(f"Your total score: {user_score}")        


print("\nComputer Batting Turn:")

for i in range(turns):
    computer = int(input(f"Bowl {i+1}: Enter The Number(1-6)"))
    player = rand.randint(1,6)
    print(f"Player bowled: {player}")


    if player == computer:
        print("You are Out!")
        break
    else:
        computer_score += computer
        print(f"Run Scored {computer_score }")
print(f"Your total score: {computer_score}")  



print(f"\nFinal Score => You: {user_score} | Computer: {computer_score}")

if user_score == computer_score:
    print("Score is Tie. Play again for result")
elif user_score > computer_score:
    print(f"You Win! Your Score: {user_score}")
else:
    print(f"Computer Wins! Computer Score: {computer_score}")

import random as rand



print("============Mini-Cricket-match================\n")
print("Rules: Choose a number 1-6. If your number matches computer's number, you're OUT!")

while True:
    try:
        over = int(input("Enter how many overs you want to play: "))
        if over > 0:
            break
    except:
        print("Enter numbers only!")
user_score = 0
computer_score = 0
turns = 6 * over


print("\nYour Batting Turn:")

for i in range(turns):
    while True:
        try:
            user = int(input(f"Bowl {i+1}: Enter The Number(1-6)"))
            if 1 <= user <=6:
                break
        except:
            print("Invalid input!")
    comput = rand.randint(1,6)
    print(f"Computer bowled: {comput}")


    if user == comput:
        print("You are Out!")
        break
    else:
        user_score += user
    print(f"Run Scored {user_score}")
    if(i+1) % 6  == 0 or i == [turns-1]:
        over_played = (i+1)//6 + ((i+1) % 6) / 6
        run_rate = user_score / over_played
        print(f"\n End of Over {(i+1)//6}")  

        print(f"Run Scored {user_score}")
        print(f"Run Rate: {round(run_rate,2)}\n")


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

    if(i+1) % 6  == 0 or i == [turns-1]:
        over_played = (i+1)//6 + ((i+1) % 6) / 6
        run_rate = user_score / overs_played
        print(f"\n End of Over {(i+1)//6}")  

        print(f"Run Scored {computer_score}")
        print(f"Run Rate: {round(run_rate,2)}\n")
        print(f"Run Scored {computer_score }")
print(f"Your total score: {computer_score}")  



print(f"\nFinal Score => You: {user_score} | Computer: {computer_score}")

if user_score == computer_score:
    print("Score is Tie. Play again for result")
elif user_score > computer_score:
    print(f"You Win! Your Score: {user_score}")
else:
    print(f"Computer Wins! Computer Score: {computer_score}")

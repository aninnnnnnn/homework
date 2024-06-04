from random import choice

a = ["paper", "scissors", "rock"]

human = 0
computer = 0

while human < 3 and computer < 3:
    while True:
        human_answer = input(f"Enter Your Choice {a}: ").lower()
        if human_answer in a:
            break
        print('Incorrect!')

    computer_answer = choice(a)
    print(f"Computer: {computer_answer} / Human: {human_answer}")
    if human_answer == computer_answer:
        pass

    elif (human_answer == "scissors" and computer_answer == "rock") or (human_answer == "paper" and computer_answer == "scissors") or (human_answer == "rock" and computer_answer == "paper"):
        computer += 1

    else:
        human += 1

    print(f"Human: {human} / Computer: {computer}")

if computer > human:
    print("Human is defeated!")
else:
    print("Computer is defeated!")

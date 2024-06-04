# from random import randint
#
# a = randint(1, 300)
#
# i = 0
#
#
# # while True:
#     i +=1
#     answer = int(input("Guess: "))
#
#     if answer == a:
#         print(f"Correct! you needed {i} tries")
#         break
#
#     elif answer < a:
#         print("Greater")
#
#     else:
#         print("Less!")

table = ["?", "?", "?",
         "?", "?", "?",
         "?", "?", "?"]

def display_table():
    print(table[0] + "|" + table[1] + "|" + table[2] + "            " + "1|2|3")
    print(table[3] + "|" + table[4] + "|" + table[5] + "            " + "4|5|6")
    print(table[6] + "|" + table[7] + "|" + table[8] + "            " + "7|8|9")

def players():
    print("choose player x/0")
    player1 = input("player1: ")
    player2 = ""

    if player1 =="X":
        player2 = "0"
        print(f"player2: {player2}")

    elif player1 == "0":
        player2 = "X"
        print(f"player2: {player2}")
    else:
        print("invalid")

current_player = "x"
run = True

def player_position():
    global run
    print("current player:" + current_player)
    position = input("choose(1/9): ")

    valid = False
    while not valid:
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            position = input("choose(1/9): ")

        position = int(position) - 1

        if table[position] == "?":
            valid = True
        else:
            print("position is taken!")

    table[position] = current_player
    display_table()

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "0"
    else:
        current_player = "X"


def check_winner():
    global run
    if table[0] == table[1] == table[2] != "?":
        run = False




















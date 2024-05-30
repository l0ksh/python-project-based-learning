import random as rd

rock_table = {"paper":"lose","scissors":"win","rock":"again"}
paper_table = {"paper":"again","scissors":"lose","rock":"win"}
scissors_table = {"paper":"win","scissors":"again","rock":"lose"}
game_logic = {"rock":rock_table,"paper":paper_table,"scissors":scissors_table}
choices = ["rock","paper","scissors"]

# print(type(rock_table))
# print(type(game_logic))
# print(rock_table)
# print(game_logic["rock"]["paper"])

player_score = 0
computer_score = 0
round_number = 1

while True: #game is going
    player = input("What do you want to play (rock/paper/scissors)?:").lower()
    print(f"Round {round_number}:")
    print(f"You played {player}!")
    computer = choices[rd.randint(0,2)]
    print(f"Compute played {computer}!")
    if game_logic[player][computer] == "lose":
        print("Oh no! You Lose!")
        computer_score += 1
        if input(f"Your current score: {player_score}. Computer current score: {computer_score}. Another round? (Y/N)") == "N":
            break
    elif game_logic[player][computer] == "win":
        print("Congrats! You Win!")
        player_score += 1
        if input(f"Your current score: {player_score}. Computer current score: {computer_score}. Another round? (Y/N)") == "N":
            break
    elif game_logic[player][computer] == "again":
        print("Another round!")
        round_number += 1
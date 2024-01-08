import random

def toss():
    min_value = 1
    max_value = 6
    toss = random.randint(min_value, max_value)

    return toss

while True:
     players = input("Enter the number of players (2-5): ")
     if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
         break
        else:
         print("Must be between 2 - 5 Players.")
     else:
         print("invalid")

max_score = 50
players_score = [0 for _ in range (players)] 
print(players_score)
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

while max(players_score) < max_score:
   
        for player_indx in range(players): 
         print("\nplayer",player_indx + 1,"turn has just started!\n")
        current_score = 0
        
        while True:
            should_toss = input("Would you like to toss (y)? ")
            if should_toss.lower() !="y":
                break

            value = toss()
            if value == 1:
                print("You tossed a 1! Turn done!")
                break

            else:
             current_score += value
            print("You tossed a:", value)

            print("Your current score is:" , current_score)
        players_score[player_indx] += current_score
        print("Total score is:",players_score[player_indx])



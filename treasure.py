
print("Welcome to the treasure Island.\nyour mission is to find treasure\n")
d = input("you\'re are at a cross Road. where do you want to go? Type 'left' or 'right' ")

if d == "left" :
    e=input("You have come to a lake. There is a island in the middle of lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()

    if e == "wait" :
        g = input("you arrive at the island unharmed. There is a house with 3 doors. one red one yellow and one blue. Whcich door do you choose? ").lower()
        if g == "yellow":
            print("you have won the treasure")
        elif g == "red":
            print("Its a room of fire, Game Over")
        elif g == "blue":
            print("Zombies attacked you, Game Over")
        else:
            print("You chose a door that doesn't exist,Game over")
    else:
        print("you get attacked by crocodiles, Game Over")
else:
  print("you fell into a hole,Game Over")

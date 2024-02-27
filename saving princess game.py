print("Enchanted Escape: Quest for Love")

print("Welcome brave adventurer! Your mission is to rescue a princess from a castle. " 
      "But hold on! This ain't your typical fairytale. Along the way, "
      "you will face riddles, make buzzing choices and encounter unexpected twists. "
      "Can you navigate this enchanting journey and find true love, "
      "or will you die trying? ")
print("Your adventure begins now!")

choice1 = input("As you approach, a mystical voice challenges you with a riddle: "
                "I speak without a mouth and hear without ears. "
                "I have no body, but I come alive with the wind what am I?\n"
                'a) "fire" or b) "wind" \n').lower()
if choice1 == "wind":
  
  choice2 = input("\nThe gates creak open, allowing you to enter. "
                  "Inside the castle, you come across a hallway with three doors. "
                  "Each door has a symbol: a key, a sword, and a crown. "
                  "You can only choose one. Which door will you open.\n"
                  'Type a) "key(curiosty)" b) "sword(strength)"'
                  ' \n').lower()
  if choice2 == "key(curiosty)":
    choice3 = input("\nThe door swings open, revealing a hidden passage."
                    "As you reach the inner chamber, a fierce guardian stands "
                    "in your way. "
                    "It demands to know why you seek the princess. "
                    "What reson will you give to convince the guardian "
                    "that your intentions "
                    "are pure. "
                    'Type a) "love and compassion" b) "quest for honor" '
                    'c) "destiny and adventure" \n').lower()
    if choice3 == "love and compassion":
     print("\nThe guardian nods, moved by your sincerity and lets you pass.")
    elif choice3 == "quest for honor":
     print("\nThe guardian challenges you to a duel. Turns out, he's a master "
           "swordsman and he kills you swiflty. Game over!")
    elif choice3 == "destiny and adventure":
      print("The guardian laughs and teleports you to a distant land. "
           "You start a new adventure. Game over!(in this castle)")
    else:
      print("You did not put in correct data, thus the guardian knows your intentions "
           "are not pure and puts you in a magic bottle. Game over!")
  else:
    print("The door swings open, and an army of strong, gigantic toy soldiers attack "
         "and kill you. Game over!")
else:
  print("The castle gates burst into flames. Game over!")
    
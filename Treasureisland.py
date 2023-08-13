print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. And not to die.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input(print("You are on a cross road and there is a tree and on the bark that says 'Not all solutions are right.' The words carved into a dagger it seems. and beneath there lies a skeleton. Hmmm this made you consider there could be a dangerous end to this paths. Maybe the now skeleton could have really helped if it carved the right direction instead of riddles. But who care this is a Text RPG. Are you going to the left or right player? choose wisely."))

if direction == "right":
  print("When you were walking suddenly you start to fall in a pitt. You tried to slow your fall with your dagger but while it slowed you the dagger is stuck to the walls and it slipped from your hand. While luckily surviving you have no way to get up. And when you take a closer look at the floor -which is not very big- there lies other skeletons. At this point you could scream or shout to get some help from others. But you feel like nobody is gonna go trough this path soon. Maybe you could name a skeleton Wilson and befriend it. Until the cold death comes painfully atleast you could have a company.  **Gameover**       ")
if direction == "left":
  direction2 =input(print('You have come to a lake. There is a island in the middle of the lake. You thought to yourself well this is a game about Treasure Island maybe I should go there. You think to yourself how can I get there? but the only two choices are you could have come up with is either "swimming" to the island or "waiting" a boat to come and take you there. What are you gonna do now player? Type "swim" or "wait" in order to choose your actions.'))
  if direction2 == "wait":
    direction3 = input(print("I don't know how did you manage to do it but somehow someone took a pity on you and offered to trip to the island in the middle.*narrator is frustrated at this point* *sigh* Well player, you arrived at the island and with some dumb luck you could find 3 entrances in a boulder. There is a Green, Red and Blue door. And you thought to yourself What? Is the game this easy? Maybe I should return the game into the store but you haven't even bought this game.Which door are you going in? 'Green', 'Red', 'Blue' "))
    if direction3 =="Blue":
      print("You've got eaten by beasts. **Game over**")
    if direction3 == "Red":
      print("You burned in the fire. **Game over**")
    if direction3 == "Green":
      print("You win! I guess lol. Don't ever comeback. *the game teleports with your computer for the game is never seen again. oh you lost your computer too lol.*")
  if direction2=="swim":
    print("You somehow attacked by level 900 Carp and got killed. Then carp teabagged on you. **Game over**")


"""
Thanks for playing player.
"""

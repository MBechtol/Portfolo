import random
def rollDice(side, number):

  for userRoll in range(0,number):
    userRoll = random.randint(1, side)
    print(userRoll)

#user input   
while True:
  sideSelect = input("how many sides?  ")
  numberSelect = input("How many dice?  ")
  numberSelect = int(numberSelect)
  sideSelect = int(sideSelect)
  rollDice(sideSelect, numberSelect)
  continue

print("Caves of Madness")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

room1 = input("your in a cave. the cavern forks. do you go 'left' or 'right'?\n")

if room1 == "left" :
  print("""You choose the left tunnel. 
  After a few feet you hear a rumbling noise. 
  Suddenly the floor colapses and you plumet to your death\ngame over""")
elif room1 == "right":
  room2 = input("you choose to take the right tunnel. after a few hundered feet you come accross a underground lake. you see a sketchy looking rope bridge and a old leaky boat. do you take the'bridge' or take the 'boat'\next")
  if room2 == "bridge":
    print("you choose to take the bridge. it is rickety but you make it safley accross. on the otherside you encounter a giant spider. Hungerly it races toward you as your frozen in terror.\n  you have died \n game over.")
  elif room2 == "boat":
    sword = input("you choose the boat. as you are pushing it into the water you find a sword in the sand. do you pick it up 'Y' or 'N'\n")
    print("you make it accross the lake just fine. as your pulling the boat on shore you see a giant spider coming for you.")
    if sword.lower() == "y":
      final = input("you pull out your sword and stab at it wildly. The spider turns and flees. you continue into a large chamber inside are three chests. do you open chest 1, 2, or 3\n")
      if final == "3":
        print("You open the chest to find it is filled to the brim with gold and jewels. your are rich.")
      else:
        print("you open your chest to find it empty. the ground begans to shake and the ceiling starts to collapse. you try to run but it is to late.\n game over")
    else: 
      print("you try to flee but it is to late the spider is already upon you.\ngame over")
  else:
    print("error!!\nas your trying to decide a giant spider sneaks out of the shadows. you never saw it coming\ngame over")
else:
  print("error\n as your pace back and forth pondering what path to take you slip on the ground hitting your head against a rock\ngame over")



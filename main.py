gasTaken = 0
keysTaken = 0
doorsOpened = 0
inventory = {}
location = ""
score = 0

def gatherStoryInput():
  global gasTaken, keysTaken, doorsOpened, inventory, location
  print("")
  print("Location: " + location)
  i = input("Which direction/area do you want to go to? ")

  if i == "north":
    if location == "Jail Cell":
      print("You walk through the door and enter a long dim hallway")
      print("The hallway stretches from east to west")
      location = "Hallway (Middle)"

    elif location == "Hallway (West)":
      if doorsOpened == 1:
        print("You enter a room with a chair and a desk surrounded by bulletproof glass")
        print("There is an open door to the north")
        location = "Jail Entrance"
      else:
        print("You find a locked door. Would you like to open it?")
        i2 = input("---> ")
        if i2 == "yes":
          if "keys" in inventory:
            print("You open the door with the ring of keys and walk through")
            location = "Jail Entrance"
            doorsOpened == 1
          else:
            print("You don't have the keys")
        else:
          print("You do not attempt to open the door.")
  elif i == "south":
    if location == "Jail Cell":
      print("There nowhere to go that way.")
    elif location == "Hallway (Middle)":
      print("You head back into the jail cell")
      location = "Jail Cell"
    elif location == "Jail Entrance":
      print("You leave the jail and end up on a sandy beach")
      location = "Beach"
    elif location == "Beach":
      print("You walk directly into the ocean. I hope you can swim!")
      return False
  elif i == "east":
    if location == "Jail Cell":
      print("There nowhere to go that way.")
    elif location == "Hallway (Middle)":
      print("You reach the east end of the hallway.")
      print("There is a key ring here. Would you like to pick it up? ")
      i3 = input("---> ")
      if i3 == "yes":
        inventory["keys"] = 5
        keysTaken = 1
        print("You picked up the keys!!")
      else:
        print("You do not pick up the keys")
      location = "Hallway (East)"
    elif location == "Hallway (West)":
      print("You walk back towards the jail cell")
      location = "Hallway (Middle)"

def main():
  global gasTaken, keysTaken, doorsOpened, inventory, location, score
  location = "Jail Cell"
  score = 0
  gasTaken = 0
  inventory = {"spoon": 1}
  print("Welcome to Escape From Alcatraz!!")
  print("You awake in a dark jail cell. It is empty.")
  print("The cell door is to the North. It is ajar.")
  result = gatherStoryInput()


main()
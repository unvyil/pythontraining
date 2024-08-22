# Pass the Bomb - www.101computing.net/pass-the-bomb
import random, time

def displayBanner():
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
  print("-                             -")
  print("*        Pass the Bomb        *")
  print("-                             -")
  print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

def inputPlayers():
  players = []
  player = input("Enter the name of the first player or 'X' to exit:")

  while player!="X":
    players.append(player)
    player = input("Enter the name of the next player or 'X' stop adding new players:")
  return players


# >>> Main Code Starts Here
displayBanner()
players = inputPlayers()

if len(players)<=1:
  print("Sorry, you need at least two players to play this game...")
else:  
  
  consonants = ["B","C","D","F","G","H","I","J","K","L","M","N","P","R","S","T"] #Not included: Q, V, W, X, Y, Z
  vowels = ["A","E","I","O","U"]
  letters = random.choice(consonants) + random.choice(vowels)
  
  print("")
  print(">>> Starting game in 3...")
  time.sleep(5)
  print(">>> 2...")
  time.sleep(5)
  print(">>> 1...")
  time.sleep(5)
  print("")
  
  allocatedTime = random.randint(5,20) #A random value representing the number of seconds before the bomb explodes...
  #The clock is ticking
  startTime=time.time()
  currentPlayer = ""
  
  #Carry onplaying while there is more than one player left...
  while len(players)>1:
    #Passing the bomb to a player. Making sure the bomb does get passed on to the same player!
    passingTo = random.choice(players)
    while passingTo==currentPlayer:
      passingTo = random.choice(players)
      
    currentPlayer = passingTo
    print(">>> Passing the bomb to " +  currentPlayer)
    
    word = input(currentPlayer + ", type a word containing the letters " + letters + " :").upper()
    while letters not in word:
      print(">>> Invalid word, try again...")
      word = input(currentPlayer + ", type a word containing the letters " + letters + " :").upper()
      
    
    elapsedTime = time.time() - startTime
    # Has the bomb reached its delay?
    if elapsedTime >= allocatedTime:
      print("")
      print("<>><>>><>>>><>>")  
      print(">>< Kabooum <>>")
      print("<>><>>><>>>><>>")  
      print("")
      
      print("Sorry " +  currentPlayer + " the Bomb exploded before you could pass it to someone else. You are out!")
      print("")
      players.remove(currentPlayer)
      time.sleep(1)
      print(">>> Resetting the bomb")
      allocatedTime = random.randint(10,30)
      startTime = time.time()
      letters = random.choice(consonants) + random.choice(vowels)
      
  print("")    
  print(">>> And the winner is...")
  print(">>> " + players[0])

import random

print ("Flip coin...")

# 1 = heads, 2 = tails
coin = random.randint(1,2)

if(coin == 1):
  print ("It is heads!")
elif(coin == 2): 
  print ("It is tails!")

print ("Rolling die...")

# Exercise: Rolling dice

die = random.randint(1,6)

if (dice == 1):
  print("You rolled a 1!")
elif(dice == 2): 
  print("You rolled a 2!")
elif(dice == 3): 
  print("You rolled a 3!")
elif(dice == 4): 
  print("You rolled a 4!")
elif(dice == 5): 
  print("You rolled a 5!")
elif (dice == 6): 
  print("You rolled a 6!")

# Exercise: Rock Paper Scissors (RPS)
import random

print ("Welcome to RPS")
print ("1. rock")
print ("2. paper")
print ("3. scissors")
p1 = input("Enter your choice: ")

cpu = random.randint(1,3)

# 1 : rock , 2 : paper , 3 : scissors

# Convert 1
if (p1 == "1" or p1 == "rock"):
  p1 = 1
# Convert 2
elif (p1 == "2" or p1 == "paper"):
  p1 = 2
# Convert 3
elif (p1 == "3" or p1 == "scissors"):
  p1 = 3

# Rock vs Rock  (t)
# Rock vs Paper (l)
# Rock vs Scissors (w)

# Paper vs Rock (w)
# Paper vs Paper  (t)
# Paper vs Scissors (l)

# Scissors vs Rock (l)
# Scissors vs Paper (w)
# Scissors vs Scissors (t)

# Tied
if (p1 == cpu):
  print ("Tied")

# player won
elif (p1 == 1 and cpu == 3 or p1 == 2 and cpu == 1 or p1 == 3 and cpu == 2):
  print ("Player won")

# player lost
elif (p1 == 1 and cpu == 2 or p1 == 2 and cpu == 3 or p1 == 3 and cpu == 1):
  print ("Player lost")

if (cpu == 1):
  print ("cpu : rock")
elif (cpu == 2):
  print ("cpu : paper")
elif (cpu == 3):
  print ("cpu : scissors")








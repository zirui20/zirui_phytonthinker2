import random

health = 100
battles = 0

print("the hero starts on his adventure with 100 health!")

while health > 0:
    damage = random.randint(1,15)
    health -= damage
    battles += 1



    

    print("after fighting monsters, his health is now: " , health)


if health <= 0:
    print("he fought" , battles , "battles, and died") 

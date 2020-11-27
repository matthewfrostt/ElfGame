import random

dice_roll = random.randint(0, 7)

if (dice_roll % 2) == 0:
    print("The dice rolled an even number!")
else:
    print("The dice rolled an odd number!")


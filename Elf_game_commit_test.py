import random

dice_roll = random.randint(0, 7)

if (dice_roll % 2) == 0:
    print("Thiss rolled an even number")
else:
    print("this was not an odd")


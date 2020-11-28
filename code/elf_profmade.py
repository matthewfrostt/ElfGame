import sys
import time
def slowprint(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)
cash = 0
woods = 10
forest = 20
mountains = 50
elf_am = 10
print("Day 1!, Current Elfs = {}".format(elf_am))
print("You currently have ${} in your balance!".format(cash))
elf_s = int(input("How many Elfs would you like to send to work today?: "))
woodsp = elf_s * woods
choice = input("Pick a destination to send the Elfs to work: 1 - Woods, 2 - Forest, 3 - Mountains: ")
if choice == "1":
    slowprint("You have sent {} Elf/Elfs to the Woods and made ${} !".format(elf_s,woodsp)) 
    

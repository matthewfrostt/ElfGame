import sys
import time
def slowprint(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def send_elf():
    elf_am = 10
    elf_s = int(input("How many Elfs would you like to send?: "))
    if elf_s == 1:
        slowprint("You are sending {} elf, now you have {} elfs!".format(elf_s,elf_am - 1))
    elif elf_s == 2:
        slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 2))
    elif elf_s == 3:
        slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 3))
    elif elf_s == 4:
        slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 4))
    elif elf_s == 5:
        slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 5))
    elif elf_s == 6:
        slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 6))
    elif elf_s == 7:
        slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 7))
    elif elf_s == 8:
        slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 8))
    else:
        slowprint("Please choose a valid answer! Between 1-8")

send_elf()
#Notes - Need to try and add .format(elf_am - elf_s) have attempted, it outputs invalid syntax: unsupported operand type(s) for -: 'int' and 'str'

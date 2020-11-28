import sys
import time
def slowprint(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

elf_am = 10
elf_s = input("How many Elfs would you like to send?: ")
if elf_s == "1":
    slowprint("You are sending {} elf, now you have {} elfs!".format(elf_s,elf_am - 1))
elif elf_s == "2":
    slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 2))
elif elf_s == "3":
    slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 3))
elif elf_s == "4":
    slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 4))
elif elf_s == "5":
    slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 5))
elif elf_s == "6":
    slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 6))
elif elf_s == "7":
    slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 7))
elif elf_s == "8":
    slowprint("You are sending {} elfs, now you have {} elfs!".format(elf_s,elf_am - 8))

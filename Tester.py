import sys
import time


def slowprint(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)

while True:
    elf_choice = input("Please choose where the elfs go, forest=1, mountins=2, woods=3: ")
    if elf_choice == 1:
        slowprint("Elfs returned safely")

    elif elf_choice == 2:
        slowprint("rip, you are stupid shouldnt of done that")
    elif elf_choice == 3:
        slowprint("meh, some of them die")
    else:
        break

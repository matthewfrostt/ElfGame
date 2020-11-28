import sys
import time


def slowprint(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.06)


while True:
    elf_choice = input("Where? Woods = 1, Forest = 2, Mountain = 3: ")
    if elf_choice == "1":
        slowprint("Elfs returned safely")

    elif elf_choice == "2":
        slowprint("rip, you are stupid shouldnt of done that")
    elif elf_choice == "3":
        slowprint("meh, some of them die")
    else:
        break
        
#You forgot to put "" on the elif elf_choices areas which is why it wouldnt output after making a choice.
#Notes - Figure out a way to fix the while True: constantly looping the elic_choice = input parts, will be difficult due to us NEEDING to break after a decision is made on a certain day

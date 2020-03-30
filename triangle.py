import os

from sys import version_info

while True: 
    size = int(input("Enter size: "))

    if size > 20:
        print("Too big!!")
        continue
    elif size == 0:
        print("Too low!")
        continue
    elif size == -1:
        break
    
    i = 0
    while i <= size:
        i += 1
        print("(*)" * i)

print("\n Done")

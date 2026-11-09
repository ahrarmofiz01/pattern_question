for i in range(1,6):
    for j in range(1,i+1):
        print("#",end="")
    print()
for i in range(1,6):
    for j in range(i,6):
        print("#",end="")
    print()
n = 5

for i in range(1, n + 1):

    # Spaces
    for j in range(1, n - i + 1):
        print(" ", end="")

    # Hashes
    for j in range(1, 2*i):
        print("#", end="")
    
    

    print()
n = 5

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end="")

    for j in range(1, 2 * i):
        print("#", end="")

    print()
 
for i in range(1, n):
    for j in range(1, i + 1):
        print(" ", end="")

    for j in range(1, 2 * (n - i)):
        print("#", end="")

    print()
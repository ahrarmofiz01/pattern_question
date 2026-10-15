for i in range(0,4,1):
    for j in range(0,4,1):
        print("%",end="")
    print()
nums = [2, 3, 2, 5, 2, 3]

count = 0

for num in nums:
    if num == 2:
        count += 1

print(count)

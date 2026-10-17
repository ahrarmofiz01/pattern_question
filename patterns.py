nums=[1,1,2,3,4,5,6,6,6,6]
freq={}
for i in range(len(nums)):
    j=nums[i]
    if j in freq:
        freq[j].append(i)
    else:
        freq[j]=[i]
print(freq)
nums = [2, 3, 2, 5, 3, 2]
sum=0
for i in nums:
    sum=sum+i
print(sum)
nums=[10,20,30,40,50]
for i in range(len(nums)):
    r=nums[0]
print(r)
nums = [4, 7, 4, 9]
seen = {}

for i in range(len(nums)):
    num = nums[0]
    seen[num] = 0
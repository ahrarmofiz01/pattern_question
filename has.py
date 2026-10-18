word="aaaannnnnnnooopppllmmmdddnnncccnnnnnnnnnn"

seen={}
for i in range(len(word)):
    r=word[i]
    if r in seen:
        seen[r]=seen[r]+1
    else:
        seen[r]=1
print(seen)

  
  


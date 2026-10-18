word="ahrar"

seen={}
for i in range(len(word)):
    j=word[i]
    if j in seen:
        seen[j]= seen[j]+1
    else:
        seen[j]=1
print(seen)
  
  


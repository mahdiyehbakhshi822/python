L= [0,1,2,2,3,0,4,2]
val = 2
count = 0
M = []
for i in range(len(L)):
    if L[i]!=val:
        M.append(L[i])
        count+=1


print(count)
print(M)
        

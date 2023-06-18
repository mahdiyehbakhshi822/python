import math
m=[]
L=[]
for i in range(1,101):
    m.append(i**2)

s = sum(m)

for j in range(1,101):
   L.append(j)
n=sum(L)**2
print(abs(s-n))
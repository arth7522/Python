a, b, c = [int(a) for a in input().split()] 
x, y, z = [int(x) for x in input().split()] 

p=[a,b,c]
q=[x,y,z]

e=f=0

for w in range(3):
    if p[w]>q[w]:
        e+=1
    elif p[w]<q[w]:
        f+=1

print(e,f)

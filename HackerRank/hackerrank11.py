a=int(input())
b=int(input())
c=int(input())
n=int(input())

x=y=z=0
list=[x,y,z]
while x<=a:
    while y<=b:
        while z<=c:
            list=[x,y,z]
            print(list,",", end ="")
            #print(list, end ="")
            z+=1
        z=0
        y+=1
    y=0
    x+=1
#list=[a,b,c]
#a="%.3d"%x
#print(a)
#-------------------------
#HackerRank Solution

#if __name__ == '__main__':
#   x = int(raw_input())
# y = int(raw_input())
#  z = int(raw_input())
#   N = int(raw_input())
#  arr = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X + Y + Z != N]
# print(arr)

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x=0
y=n-1
z=n-2
ans=0
while(x!=1):
    if(arr[y]>arr[z]):
        ans=arr[z]
        x=1
    y-=1
    z-=1
print(ans)

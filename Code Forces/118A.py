inp = input()
blank = ""
for x in range(len(inp)):
    if(inp[x]=='Y' or inp[x]=='y' or inp[x]=='A' or inp[x]=='a' or inp[x]=='E' or inp[x] =='e' or inp[x]=='I' or inp[x]=='i' or inp[x]=='O' or inp[x]=='o' or inp[x]=='U' or inp[x]=='u'):
        a=0
    else:
        blank += inp[x]
blank = blank.lower()
ans=""
for x in range(len(blank)):
    ans+="."+blank[x]
print(ans)

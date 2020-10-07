in1 = input()
in2 = input()
in1 = in1.upper()
in2 = in2.upper()
for x in range(len(in1)):
    if(ord(in1[x])>ord(in2[x])):
        ans=1
        break
    elif(ord(in1[x])<ord(in2[x])):
        ans=-1
        break
    else:
        ans=0
print(ans)

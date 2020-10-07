n=int(input());
a=0;

if n>=1 and n<=20:
    for x in range(n):
        if(a<n):
            print(a*a);
            a-=1;

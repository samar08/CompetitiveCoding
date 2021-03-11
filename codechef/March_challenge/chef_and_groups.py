t=int(input())
for te in range(t):
    s=input().rstrip()
    n=len(s)
    count=0
    i=0
    while(i<n):
        if(i==0):
            if(s[i]=='1'):
                count+=1
        else:
            if(s[i]=='1' and s[i-1]!='1'):
                count+=1
        i+=1
    print(count)
                

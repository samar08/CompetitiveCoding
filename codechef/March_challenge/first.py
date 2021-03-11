n,h,x=list(map(int,input().split(" ")))
a=list(map(int,input().split(" ")))
flag=True
if(x>=h):
    print('YES')
    flag=False
if(flag==True):
    for i in range(n):
        if(x+a[i]>=h):
            flag=False
            print('YES')
            break
    if(flag==True):
        print('NO')
        
    

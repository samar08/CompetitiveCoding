t=int(input())
for te in range(t):
    n,m=list(map(int,input().split(' ')))
    dots=n+1
    valleys=n-1
    if(valleys>=m):
        out=""
        for i in range(dots+n):
            if(i%2==0):
                out+="0"
            else:
                out+="1"
        print(dots + n)
        print(out)

    else:
        remv=m-valleys
        remdots=dots-valleys
        if(remv<=remdots):
            out=""
            n+=remv
            for i in range(n+dots):
                if(i%2==0):
                    out+="1"
                else:
                    out+="0"
            print(n + dots)
            print(out)

        else:
            out=""
            n+=remdots
            valleys+=remdots
            remv=m-valleys
            n+=remv
            valleys+=remv
            print(n+valleys)


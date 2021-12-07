t=int(input())
for te in range(t):
    f,s,t=list(input().split())
    fr,lr=list(input().split())
    if(f==fr or f==lr):
        print(f)
    else:
        print(s)
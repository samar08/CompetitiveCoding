t=int(input())
for te in range(t):
    n=int(input())
    p=input().rstrip().lower()
    out=0
    col={}
    col['o']=set('ry')
    col['p']=set('rb')
    col['g']=set('yb')
    col['a']=set('ryb')
    col['r']=set('r')
    col['y']=set('y')
    col['b']=set('b')
    col['u']=set()
    cc=[]
    for i in p:
        cc.append(col[i])
    occ=[]
    for i in range(n):
        occ.append(set())
    for i in range(n):
        for col in cc[i]:
            j=i
            flag=False
            while((j<n) and (((col in cc[j])) and (col not in occ[j]))):
                occ[j].add(col)
                j+=1
                flag=True
            #occ[i].add(col)
            if(flag==True):
                out+=1
            


    print('Case #'+str(te+1)+": "+str(out))

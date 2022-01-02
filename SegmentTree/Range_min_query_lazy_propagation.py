import sys
def buildtree(nl,nr,arr,tree,ti):
    if(nl==nr):
        tree[ti]=arr[nl]
        return
    m=nl+(nr-nl)//2
    buildtree(nl,m,arr,tree,(2*ti)+1)
    buildtree(m+1,nr,arr,tree,2*ti+2)
    tree[ti]=min(tree[2*ti+1],tree[2*ti+2])
def update(nl,nr,ti,arr,tree,lazy,l,r,val):
    if(lazy[ti]!=0):
        tree[ti]+=lazy[ti]
        if(nl!=nr):
            lazy[2*ti+1]+=lazy[ti]
            lazy[2*ti+2]+=lazy[ti]
        lazy[ti]=0
    if(l>nr or r<nl):
        return
    elif(nl>=l and nr<=r):
        tree[ti]+=val
        if(nl!=nr):
            lazy[2*ti+1]+=val
            lazy[2*ti+2]+=val
        return
    else:
        m=nl+(nr-nl)//2
        update(nl,m,2*ti+1,arr,tree,lazy,l,r,val)
        update(m+1,nr,2*ti+2,arr,tree,lazy,l,r,val)
        tree[ti]=min(tree[2*ti+1],tree[2*ti+2])
    
    
def query(nl,nr,ti,arr,tree,lazy,l,r):
    if(lazy[ti]!=0):
        tree[ti]+=lazy[ti]
        if(nl!=nr):
            lazy[2*ti+1]+=lazy[ti]
            lazy[2*ti+2]+=lazy[ti]
        lazy[ti]=0
    if(l>nr or r<nl):
        return sys.maxsize
    elif(nl>=l and nr<=r):
        return tree[ti]
    else:
        m=nl+(nr-nl)//2
        ans1=query(nl,m,2*ti+1,arr,tree,lazy,l,r)
        ans2=query(m+1,nr,2*ti+2,arr,tree,lazy,l,r)
        return min(ans1,ans2)

    


    
if __name__=='__main__':
    print('Enter no. of elements in array')
    n=int(input())
    #arr=[]
    print('Enter array elements')
    arr=list(map(int,input().split(' ')))
    tree=[]
    lazy=[]
    for i in range(4*n):
        tree.append(0)
        lazy.append(0)
    buildtree(0,n-1,arr,tree,0)
    print(tree)
    print('Enter no. of querys')
    q=int(input())
    for i in range(q):
        print('Enter query type')
        type=int(input())
        if(type==0):
            print('Enter the range l,r which you want to update')
            l,r=list(map(int,input().split(" ")))
            print('Enter value by which you want to update the range l and r')
            val=int(input())
            update(0,n-1,0,arr,tree,lazy,l,r,val)
        else:
            print('Enter l and r')
            l,r=list(map(int,input().split(' ')))
            print('Min element from l to r is')
            print(query(0,n-1,0,arr,tree,lazy,l,r))

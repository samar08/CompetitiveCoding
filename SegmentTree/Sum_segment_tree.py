def buildtree(nl,nr,arr,tree,ti):
    if(nl==nr):
        tree[ti]=arr[nl]
        return
    m=nl+(nr-nl)//2
    buildtree(nl,m,arr,tree,(2*ti)+1)
    buildtree(m+1,nr,arr,tree,2*ti+2)
    tree[ti]=tree[2*ti+1]+tree[2*ti+2]
def update(nl,nr,ti,arr,tree,idx,val):
    if(nl==nr):
        tree[ti]=val
        arr[idx]=val
        return
    m=nl+(nr-nl)//2
    if(idx<=m):
        update(nl,m,2*ti+1,arr,tree,idx,val)
    else:
        update(m+1,nr,2*ti+2,arr,tree,idx,val)
    tree[ti]=tree[2*ti+1]+tree[2*ti+2]
def query(nl,nr,ti,arr,tree,l,r):
    if(r<nl or l>nr):
        return 0
    if(l<=nl and r>=nr):
        return tree[ti]
    m = nl + (nr - nl) // 2
    ans1=query(nl,m,2*ti+1,arr,tree,l,r)
    ans2=query(m+1,nr,2*ti+2,arr,tree,l,r)
    return ans1+ans2
if __name__=='__main__':
    print('Enter no. of elements in array')
    n=int(input())
    #arr=[]
    print('Enter array elements')
    arr=list(map(int,input().split(' ')))
    tree=[]
    for i in range(4*n):
        tree.append(0)
    buildtree(0,n-1,arr,tree,0)
    print(tree)
    print('Enter no. of querys')
    q=int(input())
    for i in range(q):
        print('Enter query type')
        type=int(input())
        if(type==0):
            print('Enter index which you want to update')
            idx=int(input())
            print('Enter value of the index')
            val=int(input())
            update(0,n-1,0,arr,tree,idx,val)
        else:
            print('Enter l and r')
            l,r=list(map(int,input().split(' ')))
            print('Sum of elements from l to r is')
            print(query(0,n-1,0,arr,tree,l,r))



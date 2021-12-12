s=input().strip()
n2=len(s)
n=n2//2
arr=[set() for i in range(10)]
i=0
for j in range(n):
    arr[int(s[i+1])].add(s[i])
    i+=2
count=0
for i in range(n):
    if(len(arr[i])==3):
        count+=1
print(count)
        

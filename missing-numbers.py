# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
arr = [int(i) for i in raw_input().strip().split()]
m=int(raw_input())
array = [int(j) for j in raw_input().strip().split()]
ar=sorted(arr)
arra=sorted(array)
j=0
b=-1
i=0
while(i<m):
    j=b+1
    while(j<n):
        if(arra[i]==ar[j]):
            arra[i]=0
            b=j
            break
        if(arra[i]<ar[j]):
            j=j+1
    i=i+1
if(arra[0]!=0):
    print arra[0],
for j in range(1,m):
    if(arra[j]!=0 and arra[j]!=arra[j-1]):
        print arra[j],

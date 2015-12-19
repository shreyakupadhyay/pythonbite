# Enter your code here. Read input from STDIN. Print output to STDOUT
total = input()
arr = [int(i) for i in raw_input().strip().split()]
j=0
k=0
count=1
arr.sort()
while(j<len(arr) and k<len(arr)):
    if(arr[j]<=arr[k] and arr[k]<=arr[j]+4):
        k=k+1
        #print k,"k"
    else:
        count = count +1
        j=k
        #print j,"j"
print count

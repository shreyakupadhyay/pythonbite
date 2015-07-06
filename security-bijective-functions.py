# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(raw_input())
arr = [int(i) for i in raw_input().strip().split()]
array=sorted(arr)
c=1
for i in range(0,len(arr)):
    if(array[i]==i+1):
        continue
    
    else:
        c=0
        break
        
if(c==0):
    print "NO"

if(c==1):
    print "YES"
    
    

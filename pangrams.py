# Enter your code here. Read input from STDIN. Print output to STDOUT
n=raw_input()
count=0
a=1
arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(0,26):
        if (arr[i] in n.lower()):
            count=count+1
            continue
        elif(arr[i] not in n.lower()):
            a=0
            break
if(a==0):
    print "not pangram"
else:
    print "pangram"
        

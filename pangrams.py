# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
n=raw_input()
count=0
counter=1
arr = list(string.ascii_lowercase)
for alphabet in arr:
        if (alphabet in n.lower()):
            count=count+1
            continue
        elif(alphabet not in n.lower()):
            counter=0
            break
if(counter==0):
    print "not pangram"
else:
print "pangram"

# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(raw_input())
b=raw_input()
c=int(raw_input())
d=c%26
arr=[]
for i in range(0,a):
    if(ord(b[i])>= 65 and ord(b[i])<= 90):
        if(ord(b[i])+d >90):
            arr.append(chr(ord(b[i])+d-26))
        else:
            arr.append(chr(ord(b[i])+d))
    if(ord(b[i])>=97 and ord(b[i])<=122):
        if(ord(b[i])+d >122):
            arr.append(chr(ord(b[i])+d-26))
        else:
            arr.append(chr(ord(b[i])+d))
    if(ord(b[i])>122 or ord(b[i])<65): 
        arr.append(chr(ord(b[i])))
    if(ord(b[i])> 90 and ord(b[i]) < 97):
        arr.append(chr(ord(b[i])))
import sys
for i in range(0,a):
    sys.stdout.write(arr[i])   
 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
arr=raw_input()
e=int(raw_input())
array=[]
for i in range(0,len(arr)):
    if(chr(ord(arr[i])+e)>'9'):
        array.append(chr(ord(arr[i])+e-10))
    elif(chr(ord(arr[i])+e)>'z'):
        array.append(chr(ord(arr[i])+e-26))
    else:
        array.append(chr(ord(arr[i])+e))

for i in range(0,len(arr)):
	sys.stdout.write(array[i])

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
arr=raw_input()
array=[]
for i in range(0,len(arr)):
	if(arr[i]>='0' and arr[i]<'9'):
		array.append(chr(ord(arr[i])+1))
	if(arr[i]<'z' and arr[i]>='a'):
		array.append(chr(ord(arr[i])+1))
	if(arr[i]=='z'):
		array.append('a')
	if(arr[i]=='9'):
		array.append('0')

for i in range(0,len(arr)):
	sys.stdout.write(array[i])

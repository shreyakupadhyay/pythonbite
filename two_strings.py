# Enter your code here. Read input from STDIN. Print output to STDOUT
test_case=input()
for i in range(0,test_case):
    first=raw_input()
    second=raw_input()
    length_first=len(first)
    length_second=len(second)
    #if(length_first<=length_second):
    counter=0
    for j in range(0,26):
        #print chr(ord('a')+j)
    	if(chr(ord('a')+j) in first and chr(ord('a')+j) in second):
    		counter=1
    		break
    if(counter==1):
        print "YES"
    if(counter==0):
        print "NO"
   		#if(chr(ord('a')+i) in first and chr(ord('a')+i) in second):
   		#	counter=1
   		#	break
           #if(counter==0):
   		#print "NO"
   	#if(counter==1):
   	#	print "YES"
    #if(length_first>length_second):
    #	counter=0
    #	for i in range(0,length_second):
    #		if(second[i] in first):
    #			counter=counter+1
    #			continue
    #	if(counter>0):
    #		print "YES"
    #	if(counter==0):
    #		print "NO"

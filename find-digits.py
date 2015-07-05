# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(raw_input())
for i in range(0,t):
    a=raw_input()
    b=[]
    d=[]
    for i in range(0,len(a)):
    	d.append(a[i])

    for i in range(0,len(a)):
        b.append(a[len(a)-1-i])

    #print b
    #print d
    #print len(a)
    c=1
    for j in range(0,(len(a)-1)):
		
		m=ord(b[j+1])-ord(b[j])
		n=ord(d[j+1])-ord(d[j])
		if(m<0 and n<0):
			m = -m
			n = -n
			if(m!=n):
				c=0
				print "Not Funny"
				break
			
		if(m>=0 and n<0):
			n = -n
			if(m!=n):
				c=0
				print "Not Funny"
				break

		if(m<0 and n>=0):
			m = -m
			if(m!=n):
				c=0
				print "Not Funny"
				break		
					

		if(m>=0 and n>=0):
			if(m!=n):
				c=0
				print "Not Funny"
				break

    if c!=0:
    	print "Funny"
   	
   		

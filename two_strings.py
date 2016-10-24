test_case=input()

for num in range(0,test_case):
    first=raw_input()
    second=raw_input()
    len_first=len(first)
    len_second=len(second)
    counter=0
    for alpha_val in range(0,26):
        if(chr(ord('a')+alpha_val) in first and chr(ord('a')+alpha_val) in second):
            counter=1
            break
    if(counter==1):
        print "YES"
    if(counter==0):
        print "NO"

a=int(raw_input())
for i in range(0,a):
    arr=raw_input()
    array=raw_input()
    newstr=[]
    c=1
    ar=[]
    for i in range(0,len(arr)):
        ar.append(arr[i])
    #print ar
    for j in range(0,len(arr)-1):
        for k in range(j+1,len(arr)):
            if(arr[j]==arr[k]):
                c=0
                #ar.remove(arr[j])
                #newstr=ar
                ar[k]='a'
    for i in range(0,len(arr)):
        if(ar[i]!='a'):
            newstr.append(ar[i])
    #print newstr
    if(c==1):
        #for i in range(0,len(arr)):
        yes=[]
        list=[]
        for j in range(0,len(arr)):
            list.append(arr[j])
        for k in range(ord('A'),ord('Z')+1):
                if(chr(k) not in arr):
                    list.append(chr(k))
        #print list
        yes=arr
    else:
        yes=[]
        list=[]
        for j in range(0,len(newstr)):
            list.append(newstr[j])
        for k in range(ord('A'),ord('Z')+1):
                if(chr(k) not in newstr):
                    list.append(chr(k))
        #print list
        yes=newstr
    key=[]
    for i in range(0,len(array)):
        key.append(array[i])
    beta=[]
    gamma=[]
    gamma=sorted(yes)
    delta=[]
    #print gamma
    #for i in range(0,len(yes)):
        #for j in range(0,len(list)/len(yes)+1):
    for i in range(0,len(yes)):
        for j in range(0,len(yes)):
            if(gamma[i]==list[j]):
                delta.append(j)
                break
    #print delta
    pi=[]
    for i in range(0,len(yes)):
        k=0
        while(delta[i]+len(yes)*k <26):
                pi.append(list[delta[i]+len(yes)*k])
                k=k+1
    #print pi
    pin=[]
    for i in range(0,len(yes)):
        k=0
        while(delta[i]+len(yes)*k <26):
                pin.append(list[delta[i]+len(yes)*k])
                k=k+1
        pin.append(' ')
    #print pin
    #print key
    count=0
    cou=[]
    for i in range(0,len(array)):
        if(array[i]==' '):
            cou.append(count)
            count=0
        else:
            count=count+1
    #print cou


    import sys
    co=0
    final=[]
    coun=[]
    ci=0
    for i in range(0,len(cou)):
        ci=ci+cou[i]
        coun.append(ci)
    #for i in range(0,len(coun)):
    #    print coun[i]
    i=0
    #print len(coun)
    for k in range(0,len(key)):
        #print coun[i]
        for j in range(0,len(pi)):
            if(key[k]==pi[j]):
                final.append(chr(ord('A')+j))
                #sys.stdout.write(chr(ord('A')+j))
                break
            #if(key[k]==pi[j] and k==coun[i]):
                #print co
                #final.append(' ')
                #final.append(chr(ord('A')+j))
                #break
            #print k,coun[i]
        #if(k==coun[i] and i<len(cou)):
        #    i=i+1
    #print final
    for i in range(0,len(coun)):
        final.insert(coun[i]+i,' ')
        #print coun[i]
    for j in range(0,len(final)):
        sys.stdout.write(final[j])
    sys.stdout.write('\n')
    #for i in range(0,len(final)):
    #newfinal=[]
    #for k in range(0,len(final)):
    #    if(k==coun[i]):
    #        i=i+1
    #        print i
    #    else:
    #        newfinal=final[:k] + final[k:]
    #print newfinal

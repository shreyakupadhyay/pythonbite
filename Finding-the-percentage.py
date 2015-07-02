# Enter your code here. Read input from STDIN. Print output to STDOUT
dict={}
dic={}
n=int(raw_input())
for i in range(0,n):
    a, b, c, d=raw_input().split()
    b,c,d=float(b),float(c),float(d)
    e=(b+c+d)/3.0
    dict={a:e}
    dic.update(dict)
    
    
pr=raw_input()

print  "%.2f" % dic[pr]

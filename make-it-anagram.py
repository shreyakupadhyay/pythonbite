# Enter your code here. Read input from STDIN. Print output to STDOUT
first_a = raw_input()
second_a = raw_input()
first_array=[]
second_array=[]
for j in range(0,len(first_a)):
    first_array.append(first_a[j])

for k in range(0,len(second_a)):
    second_array.append(second_a[k])
    
first_array.sort()
second_array.sort()
val1 = len(first_array)
val2 = len(second_array)
count = 0
for j in range(0,len(first_array)):
    k=0
    for k in range(0,len(second_array)):
        if(first_array[j]==second_array[k]):
            second_array.remove(second_array[k])
            count = count + 1
            break
    j = j + 1

print val1 + val2 - 2*count
"""while(first_array[0] > second_array[0]):
    
if(first_array[0] > second_array[0]):
    count = count + 1
if(second_array[0] > first_array[0]):
    count = count + 1
if(first_array[len(first_array)-1] > second_array[len(second_array)-1]):
    count = count + 1
if(second_array[len(second_array)-1] > first_array[len(first_array)-1]):
    count = count + 1"""

l=[7980,22349,999,2799,229900,11101,9999,2195,9800,4999]
l.sort()
num=5
j=[]
min= -99999999
for i in range(0,len(l)-1):
    if num<len(l):
         a= l[i]
         b=l[num-1]
         if a-b>min:
            min= a-b
            f=i
            m=num-1
         else:
            min= min
    num+=1
for k in range( f,m+1):
    j.append(l[k])
      
print(l)
print(j)
print(min)

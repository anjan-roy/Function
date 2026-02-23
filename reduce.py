from functools import reduce
l=[10,20,30,40,50,60,70]

l1=reduce(lambda a,b:a+b,l)
l2=reduce(lambda a,b:a+b,range(1,101))
print(l1)
print(l2)

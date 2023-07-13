li_2=[72,32,64,15,18,28]
mod_1=list(map(lambda x:x**0.5,li_2))
print(mod_1)
li_3=[2,4,7,9,11,13,12,20]
odd=list(filter(lambda x:x%2!=0,li_3))
even=list(filter(lambda x:x%2==0,li_3))
from functools import reduce
mul= reduce(lambda x,y: x*y,li_3)
print(odd)
print(even)
print(mul)

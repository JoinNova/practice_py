'''
###Decorators 2 - Name Directory
import operator
def person_lister(f):
    def inner(people):
        #print(type(f))
        result = map(f, sorted(people, key=lambda people:int(people[2])))
        #print(type(result))
        return result
        
        #complete the function
    return inner
@person_lister
def name_format(person):
    return ("Mr. "if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__=='__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
'''
'''
###Athlete Sort

import operator
def person_lister(f):
    def inner(Athlete):
        result = map(f, sorted(Athlete, key=lambda Athlete:int(Athlete[k])))
        return result
    return inner
@person_lister
def name_format(person):
    result=str()
    for i in range(len(person)):
        result+=person[i]
        result+=' '
    return result

if __name__=='__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])    
    Athlete = [input().split() for i in range(n)]
    k=int(input())
    print(*name_format(Athlete), sep='\n')

'''
'''
###Any or All  이거 다시 풀어야됨.
#>>> any([1>0,1==0,1<0])
#True
#>>> any([1<0,2<1,3<2])
#False
#>>> all(['a'<'b','b'<'c'])
#True
#>>> all(['a'<'b','c'<'b'])
#False
n=int(input())
nlist=list(map(int, input().split()))
chk1=0
chk2=0
#print(nlist)
result=False
for i in range(len(nlist)):
    if nlist[i] > 0:
        chk1+=1
    if nlist[i]==0 or nlist[i]==1 or nlist[i]==2 or nlist[i]==3 or nlist[i]==4 or nlist[i]==5 or nlist[i]==6 or nlist[i]==7 or nlist[i]==8 or nlist[i]==9 or nlist[i]==11 or nlist[i]==22 or nlist[i]==33 or nlist[i]==44 or nlist[i]==55 or nlist[i]==66 or nlist[i]==77 or nlist[i]==88 or nlist[i]==99:
        chk2+=1
if chk1==n and chk2>=1:
    result=True

        
print(result)
'''
'''
###Sum and Prod
import numpy as np
n, m = list(map(int, input().split()))
arr=[]
for i in range(n):
    ar=list(map(int, input().split()))
    arr.append(ar)
my_array=np.array(arr)
result=np.sum(my_array, axis=0)
result=np.prod(result)
print(result)

'''
'''
###Min and Max
import numpy as np
n, m=list(map(int, input().split()))
arr=[]
for i in range(n):
    ar=list(map(int,input().split()))
    arr.append(ar)
my_array=np.array(arr)
result=np.min(my_array, axis = 1)
print(result)
result=np.max(result)
print(result)
'''
'''
###Mean, Var, and Std
import numpy as np
n, m = list(map(int,input().split()))
arr=[]
for i in range(n):
    ar=list(map(int,input().split()))
    arr.append(ar)
my_array=np.array(arr)
#np.set_printoptions(legacy='1.13')
print(np.mean(my_array, axis = 1))
print(np.var(my_array, axis = 0))
print(np.std(my_array, axis = None))
'''
'''
###Dot and Cross
import numpy as np
n=int(input())
arr=[]
for i in range(n):
    ar=list(map(int,input().split()))
    arr.append(ar)
A=np.array(arr)
arr=[]
for i in range(n):
    ar=list(map(int,input().split()))
    arr.append(ar)
B=np.array(arr)
print(np.dot(A,B))
'''
'''
###Inner and Outer
import numpy as np
A=list(map(int,input().split()))
A=np.array(A)
B=list(map(int,input().split()))
B=np.array(B)
print(np.inner(A,B))
print(np.outer(A,B))
'''
'''
###Polynomials
import numpy as np
#print numpy.poly([-1, 1, 1, 10])        #Output : [  1 -11   9  11 -10]
#print numpy.roots([1, 0, -1])           #Output : [-1.  1.]
#print numpy.polyint([1, 1, 1])          #Output : [ 0.33333333  0.5         1.          0.        ]
#print numpy.polyder([1, 1, 1, 1])       #Output : [3 2 1]
#print numpy.polyval([1, -2, 0, 2], 4)   #Output : 34
#print numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)
#Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]
n=list(map(float, input().split()))
x=int(input())

print(np.polyval(n,x))
'''
'''
###Linear Algebra
import numpy as np
n=int(input())
arr=[]
for i in range(n):
    ar=list(map(float,input().split()))
    arr.append(ar)
print(np.linalg.det(arr))
'''
'''
###Reduce Function
from fractions import Fraction
from functools import reduce
from fractions import gcd
def product(fracs):

    t=1
    for i in range(len(fracs)):
        t*=fracs[i]
        #print(t)
    #print(Fraction(t))
    
    return t.numerator,t.denominator

if __name__=='__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int,input().split())))
    result = product(fracs)
    print(*result)
'''
###XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    result={node}
    return len(result)

if __name__=='__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))



'''
###Classes: Dealing with Complex Numbers
import math
class Complex(object):
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
        print(self.real)
        print(self.imaginary)

    def __add__(self,no):
        #no+=no
        print("add입니다.")
        self.real += self.real
        self.imaginary += self.imaginary
        return self.real + self.imaginary*i

    def __sub__(self,no):
        #no-=no
        print('sub입니다.')
        return no

    def __mul__(self,no):
        print('mul입니다.')
        return no

    def __truediv__(self,no):
        print('div입니다.')
        return no

    def mod(self):
        print('mod입니다.')

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__=='__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y,x.mod(), y.mod()]),sep='\n')

'''
'''
###Zeros and Ones
import numpy

#zeros
print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]] 

print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
#Output : [[0 0]]

#ones
print numpy.ones((1,2))                    #Default type is float
#Output : [[ 1.  1.]] 

print numpy.ones((1,2), dtype = numpy.int) #Type changes to int
#Output : [[1 1]]  
'''

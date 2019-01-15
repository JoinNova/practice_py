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
'''
###Arrays
import numpy
def arrays(arr):
    par=[]
    result=[]
    arr.sort()
    for i in range(len(arr)):
        if float(arr[i])>=0:
            par.append(float(arr[i]))
        else :
            result.append(float(arr[i]))
    par.reverse()
    #print(par)
    for i in range(len(par)):
        result.append(par[i])
    return numpy.array(result,float)
#a = numpy.array([1,2,3,4,5])
#print a[1]          #2

#b = numpy.array([1,2,3,4,5],float)
#print b[1]          #2.0

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
'''
'''
###Shape and Reshape
import numpy
n=list(map(int,input().split()))
print(numpy.reshape(n,(3,3)))
'''
'''
###Transpose and Flatten
import numpy

n, m=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a=numpy.array(a)
print(numpy.transpose(a))
print(a.flatten())    
'''
'''
###Concatenate
import numpy as np

n, m, p =list(map(int,input().split()))
nl=[]
ml=[]
for i in range(n):
    nl.append(list(map(int,input().split())))
nl=np.array(nl)
for i in range(m):
    ml.append(list(map(int,input().split())))
ml==np.array(ml)
print(np.concatenate((nl,ml),axis = 0))
'''
'''
###Zeros and Ones
import numpy as np
n=list(map(int,input().split()))
if len(n)==1:
    print(np.zeros(int(n[0]), dtype = np.int))
    print(np.ones(int(n[0]), dtype = np.int))
elif len(n)==2:
    print(np.zeros((int(n[0]), int(n[1])), dtype = np.int))
    print(np.ones((int(n[0]), int(n[1])), dtype = np.int))
elif len(n)==3:
    print(np.zeros((int(n[0]), int(n[1]), int(n[2])), dtype = np.int))
    print(np.ones((int(n[0]), int(n[1]), int(n[2])), dtype = np.int))
elif len(n)==4:
    print(np.zeros((int(n[0]), int(n[1]), int(n[2]), int(n[3])), dtype = np.int))
    print(np.ones((int(n[0]), int(n[1]), int(n[2]), int(n[3])), dtype = np.int))
'''
'''
###Eye and Identity
import numpy as np

n, m=list(map(int,input().split()))
print(np.eye(n, m, k=0))
'''
'''
###Validating Roman Numerals
#regex_pattern = r"[MDCLXVI]"
#I (= 1), V (= 5), X (= 10), L (= 50),
#C (= 100), D (= 500), and M (= 1000

a = 'M{0,3}'
b = '(C[MD]|D?C{0,3})'
c = '(X[CL]|L?X{0,3})'
d = '(I[VX]|V?I{0,3})'
regex_pattern = a+b+c+d +'$'   # Do not delete 'r'.

import re
print(str(bool(re.match(thousand+hundred+ten+digit, input()))))
'''
'''
###Standardize Mobile Number Using Decorators

n=int(input())
nl=[]
for i in range(n):
    #num=input()
    if len(num)==12:
        nl.append(num)
    elif len(num)==11:
        ad=str(91)
        for j in range(1,11):
            ad+=str(num[j])
        nl.append(ad)
    elif len(num)==10:
        ad=str(91)
        for j in range(10):
            ad+=str(num[j])
        nl.append(ad)
nl.sort()
for i in range(n):
    result=nl[i]
    print("+{0} {1} {2}".format(result[:2],result[2:7],result[7:]))
'''
'''
def wrapper(f):
    #print('f={0}:{1}'.format(f,type(f)))
    def fun(l):
        #print("l={0}:{1}".format(l,type(l)))
        nl=[]
        for i in range(len(l)):
            num=l[i]
    #num=input()
            if len(num)==12:
                nl.append(num)
            elif len(num)==11:
                ad=str(91)
                for j in range(1,11):
                    ad+=str(num[j])
                nl.append(ad)
            elif len(num)==10:
                ad=str(91)
                for j in range(10):
                    ad+=str(num[j])
                nl.append(ad)
            elif len(num)==13:
                ad=str()
                for j in range(1,13):
                    ad+=str(num[j])
                nl.append(ad)
        nl.sort()
        for i in range(len(nl)):
            result=nl[i]
            print("+{0} {1} {2}".format(result[:2],result[2:7],result[7:]))
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l),sep='\n')
if __name__=='__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
'''
'''
###Words Score
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']
def score_words(words):
    ###Words Score
    import re
    #n=int(input())
    #print(words)
    l=list(words)
    #l=list(map(str,input().split()))
    #print(l)
    result=[]
    for i in range(len(l)):
        k=re.sub(r'\{\w+\}','',l[i])
        #print(k)
        result.append(str(re.sub(r'[bcdfghjklmnpqrstvwxz]','',k)))
    #print(result)
    chk=0
    for i in range(len(result)):
        if len(result[i])%2==0:
            chk+=2
        else :
            chk+=1
    score=int(chk)
    #print("%d"%score)

    return score
n=int(input())
words = input().split()
print(score_words(words))
'''
'''이거 다시해야함.
###XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree
maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if (level == maxdepth):
        maxdepth += 1        
    for child in elem:
        depth(child, level + 1)
        
if __name__=='__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = entree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(),-1)
    print(maxdepth)
'''
###Class 2 - Find the Torsional Angle
import math
class Points(object):
    def __init__(self,x,y,z):
        print("x{0}y{1}z{2}".format(x,y,z))
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    def __sub__(self, no):
        print("{0}{1}".format(no,type(no)))
        return vector(self.x-no.x, self.y-no.y, self.z-no.z)
    def dot(self, no):
        
        return self.x*no.x + self.y*no.y + self.z*no.z
    def cross(self, no):
        
        return vector(self.y*no.z-self.z*no.y, self.z*no.x-self.x*no.z, self.x*no.y-self.y*no.x)        
    def absolute(self):
        
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

    if __name__=='__main__':
        points = list()
        for i in range(4) :
            a = list(map(float,input().split()))
            points.append(a)
            
        a,b,c,d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
        x = (b-a).cross(c-b)
        y = (c-b).cross(d-c)
        angle = math.acos(x.dot(y)/(x.absolute()*y.absolute()))
        print("%.2f"% math.degrees(angle))



'''
###Classes: Dealing with Complex Numbers
import math
class Complex(object):
    def __init__(self,real,imaginary):
        self.chk=0
        self.real = real
        #self.real.append(real)
        #print(self.real)
        #print("++++++++++")
        self.imaginary = imaginary
       
        #print(self.imaginary)

    def __add__(self,no):
        #no+=no
        print("add입니다.{0}={1}".format(no,type(no)))
        self.real += self.real
        self.imaginary += self.imaginary
        return self.real + self.imaginary

    def __sub__(self,no):
        #no-=no
        print("sub입니다.{0}={1}".format(no,type(no)))
        return no

    def __mul__(self,no, chk):
        self.chk+=1
        print(chk)
        print("mul입니다.{0}={1}".format(no,type(no)))
        return no

    def __truediv__(self,no):
        print("div입니다.{0}={1}".format(no,type(no)))
        return no

    def mod(self):
        print("mod입니다.{0}={1}".format(self, type(self)))
        return self*self

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

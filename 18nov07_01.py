'''
###Piling Up!
t=int(input())
for i in range(t):
    result='No'
    n=int(input())
    nl=list(map(int,input().split()))
    mnlidx=nl.index(min(nl))
    ll = nl[:mnlidx]
    rl = nl[mnlidx+1:]
    if ll == sorted(ll,reverse=True) and rl == sorted(rl) :
        result='Yes'
    print(result)
'''
'''
        





        
        if min(nl)==nl[int((n+1)/2)]:            
            rl=nl[int((n+1)/2):]
            rl.sort()
            cl=nl[int((n+1)/2):]
            if rl==cl:
                ll=nl[0:int((n+1)/2)]
                ll.sort(reverse=True)
                cl=nl[0:int((n+1)/2)]
                if ll==cl:
                    rl.sort(reverse=True)
                    #print("rl={0}".format(rl))
                    #print("ll={0}".format(ll))
                    for j in range(len(rl)):
                        #print("rl[j]={0}".format(rl[j]))
                        #print("ll[j]={0}".format(ll[j]))
                        if rl[j]<=ll[j]:
                            result='Yes'     
        print(result)
    else:
        nl=list(map(int,input().split()))
        if min(nl)==nl[int(n/2)]:
            rl=nl[int((len(nl)+1)/2):]
            rl.sort()
            cl=nl[int((len(nl)+1)/2):]
            if cl==rl:
                ll=nl[0:int((len(nl)+1)/2)] 
                ll.sort(reverse=True)
                cl=nl[0:int((len(nl)+1)/2)]
                if cl==ll:
                    rl.sort(reverse=True)
                    #print("rl={0}".format(rl))
                    #print("ll={0}".format(ll))
                    for j in range(len(rl)):
                        #print("rl[j]={0}".format(rl[j]))
                        #print("ll[j]={0}".format(ll[j]))
                        if rl[j]<=ll[j]:
                            result='Yes'   
        print(result)
'''
'''
###Classes: Dealing with Complex Numbers
import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        print(self.real,no.real)
        print(self.imaginary,no.imaginary)
        return Complex(self.real+no.real, self.imaginary+no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real-no.real, self.imaginary-no.imaginary)
    def __mul__(self, no):
        return Complex(self.real*no.real-self.imaginary*no.imaginary, self.real*no.imaginary+self.imaginary*no.real)

    def __truediv__(self, no):
        return self.__mul__(Complex(no.real, -1*no.imaginary)).__mul__(Complex(1.0/(no.mod().real)**2, 0))


    def mod(self):
        return Complex(pow(self.real**2+self.imaginary**2, 0.5), 0)

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
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep = '\n')
'''

###Class 2 - Find the Torsional Angle
import math
class Points(object):
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __sub__(self, no):
        return Points(self.x-no.x, self.y-no.y, self.z-no.z)
    def dot(self, no):
        return self.x*no.x + self.y*no.y + self.z*no.z
    def cross(self, no):
        return Points(self.y*no.z-self.z*no.y, self.z*no.x-self.x*no.z, self.x*no.y-self.y*no.x)        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
if __name__=='__main__':
    points = list()
    for i in range(4):
        a = list(map(float,input().split()))
        points.append(a)
    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b-a).cross(c-b)
    y = (c-b).cross(d-c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    print("%.2f"%math.degrees(angle))


'''
###Default Arguments
class EvenStream(object):
    def __init__(self):
        self.current = 0
    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class Oddstream(object):
    def __init__(self):
        self.current = 1
    def get_next(self):
        to_return = self.current
        self.current+=2
        return to_return


def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())
        


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else :
        print_from_stream(n,Oddstream())
'''

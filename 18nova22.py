#food = "Python's favorate food is perl"
#print(food)
'''
a = 'abc'
b = 'efg'

c = a+b
print(c)
'''
'''
def add_string(a,b):
    return a+b
print(add_string(input(),input()))
'''
'''
def add_string(a,b):
    return a+b
print(add_string('abc','efg'))
print(add_string(5,10))
try:
    print(add_string(5,'efg'))
except:
    print('####err####')
print(add_string('5','efg'))
print(add_string(3.14,1000))
print(add_string(True,True))
print(add_string(True,False))
'''
'''

arr='Life is too short, You need Python'
print(arr[0:5])
print(arr[0:-1])
print(arr[::-1])

'''
'''
number1=7
val1 = 'I have %s apples' % number1#3
print(val1)


#n=3.141592
#print('%.3f'%m)
#print('%s'%str(m)[:5])

number2=77
val2 ='I ate {0} apples'.format(number2)
print(val2)
'''
'''
def con(arg):
    arg=str(arg)
    front=str()
    end=str()
    chk=0
    for i in range (len(arg)):
        if arg[i]=='-':
            break
        front+=arg[i]
    for i in range (len(arg)):
        if chk==1:
            end+=arg[i]
        if arg[i]=='-':
            chk=1

    return front, end
k='901231-1155247'
print(k)
print(con(k))

k='901231-1155247'.split('-')
print(k)

'''
'''
def con2(arg):
    return arg.split('-')
k='901231-1155247'
print(con2(k))
'''
'''
r1=0
r2=0
def add1(num):
    global r1
    r1 += num
    return r1

def add2(num):
    global r2
    r2 += num
    return r2

print('add1(3)={}'.format(add1(3)))
print('add1(4)={}'.format(add1(4)))
print('add2(3)={}'.format(add2(3)))
print('add2(7)={}'.format(add2(7)))
'''
'''
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self,num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()
print('cal1.add(3)={}'.format(cal1.add(3)))
print('cal1.add(4)={}'.format(cal1.add(4)))
print('cal2.add(3)={}'.format(cal2.add(3)))
print('cal2.add(7)={}'.format(cal2.add(7)))
'''
#고양이 객체를 만들어봅시다.
#고양이 이름과 색깔을 가지는 고양이를 생성해봅시다.
#고양이를 달리게 해주세요
#고양이 네로가 달리게 해주세요..
'''
class Cat:
    def __init__(self):
        self.name = '고양이'
        self.color = '하얀색'
    def eat(self):
        return '먹이를 먹다'
    def run(self):
        return '달리다'

tom = Cat()
nero = Cat()
print(tom.name)
print(tom.color)
print(tom.eat())

nero.name = '네로'
nero.color = '검은색'
act=input()
if act=='run':
    com=nero.run()
elif act=='eat':
    com=nero.eat()
print(nero.name)
print(nero.color)
print(com)
'''
'''
import os
#print(os.system('echo $PATH'))
print(os.system('firefox'))
#str1 = ''
print(os.system('env | grep LANG'))

'''
'''
import os
#print(os.environ)
#print(os.environ['PATH'])
#print(os.getcwd())
#print(os.system('dir'))
f=os.popen('dir')
print(f.read())
'''


'''
import sys, os

v1=int(sys.argv[1])
#v2=int(sys.argv[2])

#result=v1+v2
#print(result)
if v1==1:
    print(os.system('dir'))
'''
'''
import mod1

a=int(input())
b=int(input())
print(mod1.sss(a,b))
'''

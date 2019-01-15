'''
class Car:
    def __init__(self):
        self.color=0xFF0000   #바디의 색
        self.wheel_size=16    #바퀴의 크기
        self.displacement=2000#엔진 배기량
        print("Init Method")
    def forward(self): #전진
        print("전진")
#        pass
    def backward(self):#후진
        print("후진")
#        pass
    def turn_left(self):#좌회전
        print("좌회진")
#        pass
    def turn_right(self):#우회전
        print("우회진")
#        pass
#Car 클래스 정의 종료. 아래는 Car 클래스의 인스턴스를 정의하고 사용하는 코드
if __name__=='__main__':
    my_car=Car()
    print('0x{:02X}'.format(my_car.color))
    print(my_car.wheel_size)
    print(my_car.displacement)
    my_car.forward()
    my_car.backward()
    my_car.turn_left()
    my_car.turn_right()


class InstanceVar:
#    self.text_list=[]
    def __init__(self):
        self.text_list=[]
    def add(self, text):
        self.text_list.append(text)
    def print_list(self):
        print(self.text_list)
if __name__=='__main__':
    a=InstanceVar()
    a.add('a')
    a.print_list() #['a']출력을 기대
    b=InstanceVar()
    b.add('b')
    b.print_list() # ['b']출력을 기대

class ContactInfo:
    def __init__(self, name, email):
        self.name=name
        self.email=email
    def print_info(self):
        print('{0}  :  {1}'.format(self.name,self.email))
if __name__=='__main__':
    sanghyun=ContactInfo('박상현', 'eanlab@gmail.com')
    hanbit=ContactInfo('hanbit', 'noreply@hanb.co.kr')
    sanghyun.print_info()
    hanbit.print_info()
#    whoru=input('Who r U?  ')
#    urEmail=input("What's ur E-mail?  ")
#    someone=ContactInfo(whoru, urEmail)
#    someone.print_info()
'''
from my_package import module_1st
class Calculator:
    from my_package import module_1st
    @staticmethod
    def plus(a,b):
        return a+b
    @staticmethod
    def minus(a,b):
        return a-b
    @staticmethod
    def multiply(a,b):
        return a*b
    @staticmethod
    def divide(a,b):
        return a/b

if __name__=='__main__':
    print("{0}+{1}={2}".format(7,4,Calculator.plus(7,4)))
    print("{0}-{1}={2}".format(7,4,Calculator.minus(7,4)))
    print("{0}*{1}={2}".format(7,4,Calculator.multiply(7,4)))
    print("{0}/{1}={2}".format(7,4,Calculator.divide(7,4)))
    
    print("사칙연사(+,-,*,/)프로그램입니다.")

    a=module_1st.jungsu_check2()
    b=module_1st.jungsu_check3()
    mark=module_1st.mark_check()
        
    if mark=="+":
        print("{0}+{1}={2}".format(a,b,Calculator.plus(a,b)))
    elif mark=="-":
        print("{0}-{1}={2}".format(a,b,Calculator.minus(a,b)))
    elif mark=="*":
        print("{0}*{1}={2}".format(a,b,Calculator.multiply(a,b)))
    elif mark=="/":
        print("{0}/{1}={2}".format(a,b,Calculator.divide(a,b)))
'''
class InstanceCounter:
    count=0
    def __init__(self):
        InstanceCounter.count+=1
    @classmethod
    def print_instance_count(cls):
        print(cls.count)

if __name__=='__main__':
    a=InstanceCounter()
    InstanceCounter.print_instance_count()
    b=InstanceCounter()
    InstanceCounter.print_instance_count()
    c=InstanceCounter()
    c.print_instance_count()

class HasPrivate:
    def __init__(self):
        self.public="Public."
        self.__private="Private."
    def print_from_internal(self):
        print(self.public)
        print(self.__private)

이거안됨.뭔지모름 상속

class Base:
    def base_method(self):
        print("base_method")

class Derived(Base):
    print("Merong")
    pass

base=Base()
base.base_method()

derived-Derived()
derived.base_method()

class A:
    def __init__(self):
        print("A.__init__()")
        self.message="Hello"
    def print_parent(self):
        print("Parent Class")        

class B(A):
    def __init__(self):
        print("B.__init__()")

        super().print_parent()
        super().__init__()
        print("self.message is " + self.message)


if __name__=="__main__":
    b=B()



class A:
    def method(self):
        print("A")
class B(A):
    def method(self):
        print("B")
class C(A):
    def method(self):
        print("C")
class D(B,C):
    pass



class A:
    def method(self):
        print("성공")

class D:
    def method(self):
	print(A().method())
class Callable:
    def __call__(self):
	print("I am called.")

class MyDecorator:
    def __init__(self,f):
        print("Initializing MyDecorator...")
        self.func=f
    def __call__(self):
        print("Begin :{0}".format(self.func.__name__))
        self.func()
        print('End :{0}'.format(self.func.__name__))

@MyDecorator
def print_hello():
    print("Hello.")

#print_hello =MyDecorator(print_hello)


#print_hello()

if __name__=='__main__':
    print_hello()
    print("=================")
#    obj=MyDecorator(print_hello)
    print("==============")
#    obj()

#    p=print_hello
    print("===============")
#    p()



class MyRange:
    def __init__(self,start,end):
        self.current=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<self.end:
            current=self.current
            self.current+=1
            return current
        else:
            raise StopIteration()
        
for i in MyRange(0,5):
    print(i)


def YourRange(start,end):
    current=start
    while current<end:
        yield current
        current+=1
    return

for i in YourRange(0,5):
    print(i)


from abc import ABCMeta
from abc import abstractmethod
class AbstractDuck(metaclass=ABCMeta):
	@abstractmethod
	def Quack(self):
		pass
class Duck(AbstractDuck):
	pass
class Duck(AbstractDuck):
	def Quack(self):
		print("[Duck] Quack")

duck=Duck()
'''
duck.Quack()

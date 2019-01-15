
###nova_1
import math
n=int(input())
print(math.factorial(n))
###nova_2
#n=int(input())
f=1
for i in range(1,n+1) :
    f*=i
print(f) 
###nova_3
#n=int(input())
i=1
result=1
while (i<(n+1)):
    result*=i
    i+=1
print(result)

###Limks
#n=int(input('n='))
multi=1 
for i in range(1,n+1,1):
    multi=multi*i
    print(i, end="x ",)
print('=',multi)

###whals21
def solution(n):
    arr = 1     
    for i in range(1, n+1):
        arr *= i         
    return print(arr)
if __name__=='__main__':
    solution(n)

###채원
list = []
value = 0
fvalue = 0
value = '10' #input("factorial값 입력:")
if(value.isnumeric() == True):
    value = int(value)
    a = value*(value-1)
    list.append(a)
    b = a*(value-2)
    list.append(b)    
    for i in range(3,value,1):     
        b = b*(value-i)
        list.append(b) 
    print(list)
    print("factorial 결과값:",list[value-2])    
else:
    print("숫자를 입력하시오")

###ripta
def fac(v):
    if v == 1:
        return 1
    return v * fac(v-1) 
num = n
print(fac(num))

###종철
#n = int(input("입력 : "))
fact = 1 
for i in range(1, n+1, 1) :
    fact *= i 
print(fact) 

###태균
def com(a):
    r = 1
    for i in range(1 , a + 1):
        r *= i
    return r  
if __name__ == "__main__":
    v = n
    print(com(v))

###진택
#n = int(input("팩토리얼! : "))
r = 1 
for i in range(1 , n + 1):
    r *= i
print(r)

###hee3018
#n = int(input("팩토리얼 입력하세요! : "))
a = 1  
for i in range(1 , n + 1):
    a *= i
print("두구두구두구!!") 
print("결과값은") 
print(a) 
print("입니다")

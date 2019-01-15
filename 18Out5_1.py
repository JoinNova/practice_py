#랜덤한 수 5개를 자동생성하여 합계와 평균을 구하세요.
'''
import random
ran=int(input("1부터 100중 몇개의 수를 합계와 평균을 구해드릴까요?"))
rand= random.sample(range(1,101), ran)
avg = 0
total = 0

print(rand,"랜덤으로 선택된 숫자는 다음과 같습니다.")
for i in range(0,ran,1):
    total+=rand[i]
print("합계는 %d 입니다."% total)
avg=total/ran
print("평균은 %f 입니다."% avg)
'''

#random.sample()은 중복안됨 _미만 +1해야됨
#random.randrange()은 중복됨 _ 미만 +1해야됨
#random.randint()는 중복됨_ 이상 
'''
import random
 
numbers = []
 
for i in range(5) :
        numbers.append(random.randint(1,100))
        numbers.sort()
 
print(numbers)
'''

import random
 
def getNumber() :
     return random.randrange(1, 101)
 
list = []
num = 0
 
while True :
     num = getNumber()
 
     if list.count(num) == 0 :
         list.append(num)
 
     if len(list)>=5 :
          break
 
print("숫자 ==> ", end=' ')
list.sort()
for i in range(0, 5) :
    print("%d" % list[i], end= ' ')

'''
import random
 
list = []
 
for i in range(100) :
    x = random.randrange(1, 101)
    list.append(x)
 
list.sort( )
print("1부터 100까지 수에서 랜덤으로 뽑은 5가지 수의 리스트, 합계, 평균을 표시")
print("숫자 %s" %list)
print("합계 %s" %sum(list))
print("평균 %s" %(sum(list)/len(list)))
'''

'''
#C to F (섭씨를 화씨를 구하는 프로그램입니다.)
print("섭씨 온도(℃)를 화씨온도로 변환해주는 프로그램입니다.")
cel = float(input("섭씨(℃) 온도를 입력해주세요."))
fah = 0

fah = (9/5 * cel) + 32

print("입력하신 %0.1f ℃ 는 변환시  %0.1f ℉ 입니다."%(cel, fah))
'''
'''
#http://projecteuler.net/problem=1
[문제]
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
[번역]
10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
1000미만의 자연수에서 3,5의 배수의 총합을 구하라.
'''

three=0
five=0
threetofive=0
for i in range(3,1000,3):
    three+=i
for i in range(5,1000,5):
    five+=i
for i in range(15,1000,15):
    threetofive+=i
total = three + five - threetofive
print(total)

'''
x=sum(list([x for x in range(1000) if x%3==0 or x%5==0]))
print(x)
'''
'''
set3 = set(range(3, 1000, 3))
set5 = set(range(5, 1000, 5))

print(sum(set3 | set5))
'''

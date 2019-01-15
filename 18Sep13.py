##18Sep13
##복합대입연산자 결과를 간단하게 나오게하기위해


##변수선언부분
Money,c500,c100,c50,c10=0,0,0,0,0

##MainCode Part
Money=int(input("교환할 돈은 얼마?"))

c500=Money//500
Money%=500

c100=Money//100
Money%=100


c50=Money//50
Money%=50

c10=Money//10
Money%=10

##PrintCode
print("\n 오백원짜리==>%d개"%c500)
print("백원짜리==>%d개"%c100)
print("오십원짜리==>%d개"%c50)
print("십원짜리==>%d개"%c10)
print("바꾸지 못한 잔돈==>%d \n"%Money)

##초를 몇일 몇시간 몇분 몇초 로 변환 어플
##변수선언부분
Time,Day,Hour,Min=0,0,0,0
##MainCode
Time=int(input("시간환산 프로그램입니다. 몇초가 궁금하신가요?"))
Day=Time//86400
Time%=86400

Hour=Time//3600
Time%=3600

Min=Time//60
Time%=60

##PrintCode
print("\n %d일 %d시간 %d분 %d초\n"%(Day,Hour,Min,Time))

##교수님꺼
seconds,days,hours,minutes=0,0,0,0
seconds=int(input("초를 입력하세요 :"))

hours=seconds//3600
seconds%=3600

days=hours//24
hours%=24

minuates=seconds//60
seconds%=60

print("\n %d일 %d시간 %d분 %d초\n"%(days,hours,minuates,seconds))


##비트연산자
##해당 비트LED만 꺼줄떄 사용 단순작업용에해당
bit=0xff
print("5bit bitClear")
bit&=~(0x1<<5)
print("{0},{1}".format(bin(bit),hex(bit)))

print("6,3bit bits clear")
bit&=~((0x1<<6)|(0x1<<3))
print("{0},{1}".format(bin(bit),hex(bit)))

print("6,3bit bits clear,after 6bit set again")
bit|=(0x1<<6)
print("{0},{1}".format(bin(bit),hex(bit)))

##Detecting 4Bit  참또는 거짓으로만 찾을수있음
if(bit&0x1<<4):
    print("True")
else:
    print("False")
##^ 익스클로시브or 사용하기
print("6bit Invert")
bit^=(0x1<<6)
print("{0},{1}".format(bin(bit),hex(bit)))
bit^=(0x1<<6)
print("{0},{1}".format(bin(bit),hex(bit)))

##리스트는 읽고쓰기가 가능한 메모리 인덱스번호는 언제나 0부터 시작
##특정데이터를 배열해서 저장한 메모리영역에서 읽고 쓰기가 가능하게 함
##문자열, 정수, 실수 전부다 사용가능 그러나 같은종류의 조합으로만 꾸며야함.
##문자만, 숫자만,같은종류의데이터만으로 구성해야함

##remove()  pop()
##스텍 LastInFirstOut구조  POP 별말없으면 끝부터제거 스텍은 꺼내오면 사라진다.
##Index 요소의 번호(위치)를 인덱스라고한다.
##Count 리스트안에 있는 갯수
##sort()오름차순정렬 reverse=True 내림차순
##reverse() 반대로 뒤집는다.

##반복을 하는거라면 반목문을 사용하는것이편하다.
##for(초기문은 변수 사용 i=0구구단시1은 없으므로 2부터 시작,
##      비교문i<6,증감문i++1씩 증가한다.)

##for문 연습
nums=[0,0,0,0,0]

for i in range(0,5,1):
    nums[i]= int(input("정수를 입력하시오^^"))

for i in range(0,5,1):
        print("nums[%d] value %d" %(i,nums[i]))

##사용자로부터 5개의 정수를입력받아서 리스트에저장
##입력받은 5개의 합을 구한다.
##입력받은 5개의 값을 오름차순으로 정렬
##합을 리스트에 추가한다.
##그후에 리스트를오름차순으로 출력한다.


##변수선언부분
nums=[0,0,0,0,0]
Total=0

##MainCode Part
for i in range(0,5,1):
    nums[i]= int(input("정수를 입력하시오^^"))
    
Total=nums[0]+nums[1]+nums[2]+nums[3]+nums[4]

print("합은 %d"% Total)

nums.insert(5,Total)
nums.sort()


##PrintCode
print("오름차순으로 정렬하면 아래와같음.")
print('%d, %d, %d, %d, %d, %d'% (nums[0],nums[1],nums[2],nums[3],nums[4],nums[5]))


##교수님꺼
nums=[]
hap=0
size=int(input("size의 크기를 넣어주세요."))

for i in range(0,size,1) :
    nums.append(0)

print("%d개의정수를 입력하시오"% size)

for i in range(0,len(nums),1) :
    print("%d번째 입력 :"%(i+1), end="")
    nums[i]=int(input())
    hap+=nums[i]
print("입력된 정수의 합 %d"%hap)

nums.append(hap)
nums.sort()

for i in range(0,len(nums),1) :
    print("오름차순 정렬된 nums[%d] value %d"%(i,nums[i]))

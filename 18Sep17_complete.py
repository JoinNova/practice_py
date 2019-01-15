#18Sep17
#1-100까지더하기 break 또는 continue

#sum =0
#for i in range(1,101,1):
#    if(i==50) :
#        break
#    if(i%2==0) :
#        continue
#    else :
#        sum+=i
#print("for sum value is %d"% (sum))

#for를  while로 변환하기

#sum=0
#i=0
#while i!=101 :
#교수님꺼
#while i<101
#    i+=1
#    if(i==50) :
#        break
#    if(i%2==0) :
#        continue
#    sum+=i
#교수님꺼
#    else :
#        sum+=i
#print("while sum value is %d"% (sum))
#################################

##함수로 코드 간추리
#함수의 정의_함수의 이름 함수의 매개변수_ 몸체와 헤더부분을 함수라한다.
#def print(매개변수)←
#                   ↑
#print("인자")->입력-↑

#입력->매개변수 ----(몸체(함수_작업))----->결과---->출력

#def sum(a,b) :
#    c=a+b
#    return c
#print(c)

#변수이름이 숫자로 시작하면안된다.

#함수의 4가지 유형

#1. 매개변수와 리턴값이 있는 함수

# def BigData(a,b) : --->>매개변수
#           함수의 몸체
#           return c--->리턴값
# ex) input함수
#--->result=BigData(10,20)

#2. 매개변수는 존재, 리턴값이 없는 함수
# def BigData(a,b) :  -->>매개변수
#           함수의 몸체
# ex) print함수
#----->BigData(10,20)

#3. 매개변수 없지만 리턴값이 있는 함수
# def BigData() :
#           함수의 몸체
#           return 값
# ex)
#----------->result=Bigdata()

# 4. 매개변수와 리턴값이 둘다 없는 함수
# def BigDate() :
#           함수의 몸체
# ex)Hello world같은 함수
#-------->BigData()


##함수로 만들어보자 ch09

##변수선언부분



##함수정의부분
def sort(argc, *argv) :
    sort_nums = []
    for i in range(0,argc,1):
        a=argv[i]
        sort_nums.append(a)
    sort_nums.sort()
    return sort_nums
    
def reverse(argc, *argv) :
    reverse_nums = []
    for i in range(0,argc,1):
        a=argv[i]
        reverse_nums.append(a)
    reverse_nums.sort(reverse=True)
    return reverse_nums
    
def total(argc, *argv) :
    total_nums = []
    hap=0
    for i in range(0,argc,1):
        a=argv[i]
        total_nums.append(a)
        hap+=total_nums[i]
    return hap

def hapsort(argc, *argv) :
    hap_nums = []
    hap=0
    for i in range(0,argc,1):
        a=argv[i]
        hap_nums.append(a)
        hap+=hap_nums[i]
    hap_nums.append(hap)
    return hap_nums


def input_numbers(argc) :
    nums = []
    count=0

    for i in range(0,argc,1) :
        nums.append(0)

    while(count<argc) :
        print("%d번째 입력 :"%(count+1), end="")
        check=input()

        if(check.isnumeric()==True) :
            nums[count]=int(check)
            count+=1
        else :
            print("===================================")
            print("숫자가 아닙니다. 숫자를 입력하세요.")



            
    while True :
        cmd=0
        print("입력된값을 어떻게 처리할까요?")
        print("1.리스트를 오름차순으로 정렬")
        print("2.리스트를 내림차순으로정렬")
        print("3.합계를출력")
        print("4.합계를 리스트에추가한것을출력")
        print("5.프로그램종료")
        print("===================================")

        print("명령을 입력하세요.", end="")
        cmd2=input()
        if(cmd2.isnumeric()==True) :
            cmd=int(cmd2)
        else :
            print("===================================")
            print("숫자가 아닙니다. 숫자를 입력하세요.")
        

        if cmd==1 :
            print("1.리스트를 오름차순으로 정렬")
            print(sort(argc, *nums))
        elif cmd==2 :
            print("2.리스트를 내림차순으로정렬")
            print(reverse(argc, *nums))
        elif cmd==3 :
            print("3.합계를출력")
            print(total(argc, *nums))
        elif cmd==4 :
            print("4.합계를 리스트에추가한것을출력")
            print(hapsort(argc, *nums))
        elif cmd==5 :
            break
        else :
            print("===================================")
            print("명령은 1,2,3,4,5만 가능합니다.")
    print("===================================")
    print("5번 명령으로인해 프로그램을 종료합니다.")
            
##메인코드부분

if __name__ =='__main__' :

    while True :
        print("List의 크기를 입력하세요 : ", end="")
        size2=input()
        if(size2.isnumeric()==True) :
            size=int(size2)
            break
        else :
            print("===================================")
            print("숫자가 아닙니다. 숫자를 입력하세요.")


    input_numbers(size)









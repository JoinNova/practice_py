##18Sep14 파이썬시작
##전일한 for문 while 문으로 수정하기
##nums=[]
##hap=0
##count=0

##size=int(input("size의 크기를 넣어주세요."))

##for i in range(0,size,1) :
##    nums.append(0)

##print("%d개의정수를 입력하시오"% size)

##for i in range(0,len(nums),1) :
##    print("%d번째 입력 :"%(i+1), end="")
##    check=input()
##    if(check.isnumeric()==True) :
##        nums[i]=int(check)
##        hap+=nums[i]
##        count+=1
##    else :
##       print("숫자가 아닙니다. 숫자를 입력하세요.")
 
##print("입력된 정수의 합 %d"%hap)

#nums.append(hap)
#nums.sort()

#for i in range(0,len(nums),1) :
#    print("오름차순 정렬된 nums[%d] value %d"%(i,nums[i]))

#################

#정수를 입력받은대로 리스트에 저장한다.
#또다시입력을입력받는다.(명령)
#1.리시트를 오름차순으로 정렬
#2.리스트를 내림차순으로정렬
#3.합계를출력
#4.합계를 리스트에추가한것을출력
#5. 프로그램종료



#실수정렬은 안될까???

nums=[]
hap=0
count=0
print("정수정렬 프로그램입니다.")
while True :
    print("정렬하고싶은 숫자 갯수를 넣어주세요 : ", end="")
    size2=input()
    if(size2.isnumeric()==True) :
        size=int(size2)
        break
    else :
        print("숫자가 아닙니다. 숫자를 입력하세요.")



for i in range(0,size,1) :
    nums.append(0)
#print(nums)
print("%d개의정수를 입력하시오"% size)


while(count<size) :
    print("%d번째 입력 :"%(count+1), end="")
    check=input()

    if(check.isnumeric()==True) :
        nums[count]=int(check)
        hap+=nums[count]
        count+=1
    else :
        print("숫자가 아닙니다. 숫자를 입력하세요.")

#print(nums)       
#import sys
command=0
#while True :
#보통 while문은 무한반복을 시키는 포괄적인 조건을 주고 중간에 조건이 맞으면
#탈출하게한후 다른 프로그램을 계속진행하거나 종료시킨다.
while((command!="5")) :    
    print("1.리스트를 오름차순으로 정렬")
    print("2.리스트를 내림차순으로정렬")
    print("3.합계를출력")
    print("4.합계를 리스트에추가한것을출력")
    print("5.프로그램종료") 
    print("명령번호를 입력해주세요. :", end="")
    command=input()

    if(command=="1") :
        
        nums.sort()
        for i in range(0,len(nums),1) :
            print("오름차순 정렬된 nums[%d] value %d"%(i,nums[i]))

    elif(command=="2") :
        nums.sort(reverse=True)
        for i in range(0,len(nums),1) :
            print("내림차순 정렬된 nums[%d] value %d"%(i,nums[i]))

    elif(command=="3") :
        print("합은 %d"% hap)

    elif(command=="4") :
        nums.append(hap)
        for i in range(0,len(nums),1) :
            print("합계가 추간된자료  nums[%d] value %d"%(i,nums[i]))
#    elif(command=="5") :
#        sys.exit()

#        break
#sys 엑시트는 중간에 프로그램을 중단하는기능으로 정상적인 작동을 의미하지는 않는다.
#break를 써서 반복문을 탈출한후 프로그램을 작동하는것이 정상적으로 종료하는것이다.
    
#        print(nums)
            
print("5 입력으로 프로그램을 종료합니다.이용해주셔서 감사합니다.")
#import sys
#sys.exit()

##변수선언부분
##함수정의부분
##메인코드부분


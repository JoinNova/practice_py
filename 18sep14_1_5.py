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

nums=[]
hap=0
count=0
size=int(input("size의 크기를 넣어주세요."))

for i in range(0,size,1) :
    nums.append(0)

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
print("1.리시트를 오름차순으로 정렬")
print("2.리스트를 내림차순으로정렬")
print("3.합계를출력")
print("4.합계를 리스트에추가한것을출력")
print("5.프로그램종료") 
command=int(input("명령을입력해주세요."))
if(command==1) :
    nums.sort()
    for i in range(0,len(nums),1) :
        print("오름차순 정렬된 nums[%d] value %d"%(i,nums[i]))
##elif로 수정해야함.와일끝 재귀함수로무한루프해야함.
elif(command==2) :
    nums.sort(reverse=True)
    for i in range(0,len(nums),1) :
        print("내림차순 정렬된 nums[%d] value %d"%(i,nums[i]))
elif(command==3) :
    print("합은 %d"% hap)
elif(command==4) :
    nums.append(hap)
    for i in range(0,len(nums),1) :
        print("합계가 추간된자료  nums[%d] value %d"%(i,nums[i]))
elif(command==5) :
    import sys
    sys.exit()
else :
    print("명령은 주어진1,2,3,4,5만 입력해주세요.")
    command=int(input("명령을입력해주세요."))
    command=int(input("명령을입력해주세요."))
    if(command==1) :
        nums.sort()
        for i in range(0,len(nums),1) :
            print("오름차순 정렬된 nums[%d] value %d"%(i,nums[i]))
    elif(command==2) :
        nums.sort(reverse=True)
        for i in range(0,len(nums),1) :
            print("내림차순 정렬된 nums[%d] value %d"%(i,nums[i]))
    elif(command==3) :
        print("합은 %d"% hap)
    elif(command==4) :
        nums.append(hap)
        for i in range(0,len(nums),1) :
            print("합계가 추간된자료  nums[%d] value %d"%(i,nums[i]))
    else :
        import sys
        sys.exit()
            




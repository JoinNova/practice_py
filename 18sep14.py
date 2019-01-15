##18Sep14 파이썬시작

##전일한 for문 while 문으로 수정하기
#nums=[]
#hap=0
#count=0

#size=int(input("size의 크기를 넣어주세요."))

#for i in range(0,size,1) :
#    nums.append(0)

#print("%d개의정수를 입력하시오"% size)

#for i in range(0,len(nums),1) :
#    print("%d번째 입력 :"%(i+1), end="")
#    check=input()
#    if(check.isnumeric()==True) :
#        nums[i]=int(check)
#        hap+=nums[i]
#        count+=1
#    else :
#        print("숫자가 아닙니다. 숫자를 입력하세요.")
 
#print("입력된 정수의 합 %d"%hap)

#nums.append(hap)
#nums.sort()

#for i in range(0,len(nums),1) :
#    print("오름차순 정렬된 nums[%d] value %d"%(i,nums[i]))

#################
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
 
print("입력된 정수의 합 %d"%hap)

nums.append(hap)
nums.sort()

for i in range(0,len(nums),1) :
    print("오름차순 정렬된 nums[%d] value %d"%(i,nums[i]))

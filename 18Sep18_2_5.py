def sort(argc, *argv) :
    nums = []
    for i in range(0,argc,1):
        a=argv[i]
        nums.append(a)
#    nums.sort()
#for 문에서 (시작값,끝날값,증가값) 이지만 (끝날값)만 입력해도 돌아간다.

            
    for i in range(len(nums)-1):
        for i in range(len(nums)-1):
#    for i in range(0,argc-1,1):
#        for i in range(0,argc-1,1):
            if nums[i]>nums[i+1]:
#                temporary=nums[i]
#                nums[i]=nums[i+1]
#                nums[i+1]=temporary
                (nums[i],nums[i+1])=(nums[i+1],nums[i])
    return nums
    
def reverse(argc, *argv) :
    reverse_nums = []
    for i in range(0,argc,1):
        a=argv[i]
        reverse_nums.append(a)
#    reverse_nums.sort(reverse=True)
    for i in range(len(reverse_nums)-1):
        for i in range(len(reverse_nums)-1):
#    for i in range(0,argc-1,1):
#        for i in range(0,argc-1,1):
            if reverse_nums[i]<reverse_nums[i+1]:
                temporary=reverse_nums[i]
                reverse_nums[i]=reverse_nums[i+1]
                reverse_nums[i+1]=temporary
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

        
def input_numbers(arg):
    nums=[]
    count=0

    for i in range(0,arg,1):
        nums.append(0)
    while(count<arg):
        print("%d번째 정수값 입력:"% (count+1),end="")
        chk= input()
        if(chk.isnumeric()==True):
            nums[count]=int(chk)
            count+=1
        else:
            print("숫자가 아닙니다. 숫자를 입력하세요.")
    return nums

def menu():
    while True:
        
        print("===================================")
        print("입력된값을 어떻게 처리할까요?")
        print("1.리스트를 오름차순으로 정렬")
        print("2.리스트를 내림차순으로정렬")
        print("3.합계를출력")
        print("4.합계를 리스트에추가한것을출력")
        print("5.프로그램종료")
        print("===================================")

        print("명령번호를 숫자로 입력해주세요. : ", end="")
        sel2=input()
        if(sel2.isnumeric()==True) :
            sel=int(sel2)
            break
        else :
            print("명령어를 잘못 입력하셨습니다. 1,2,3,4,5중 입력해주세요.")

    
    return sel        

#####메인함수##########
if __name__=='__main__':
    print("정수를 정렬해주는 프로그램입니다.")

    while True :
        print("정렬하고싶은 정수의 갯수를 입력하세요 : ", end="")
        size2=input()
        if(size2.isnumeric()==True) :
            size=int(size2)
            break
        else :
            print("===================================")
            print("숫자가 아닙니다. 숫자를 입력하세요.")


    TestList = input_numbers(size)

    while True :
        cmd=menu()

        if cmd==1:
            print("오름차순정렬은아래와 같습니다.")  
            print(sort(size,*TestList))
        elif cmd==2:
            print("내림차순정렬은아래와 같습니다.")            
            print(reverse(size,*TestList))
        elif cmd==3:
            print("합은 %d 입니다."% total(size,*TestList))
        elif cmd==4:
            print("합이 추가된 정렬은아래와 같습니다.") 
            print(hapsort(size,*TestList))
        elif cmd==5:
            break

    print("5번 명령으로인해 프로그램을 종료합니다.")


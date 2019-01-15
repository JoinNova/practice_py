def sort(argc, *argv) :
    sort_nums = []

    for i in range(0, argc, 1) :
        a = argv[i]
        sort_nums.append(a)

    sort_nums.sort()

    return sort_nums

def input_numbers(argc) :
    nums = []
    count = 0

    for i in range(0, argc, 1) :
        nums.append(0)

    while(count < argc) :
        print("%d 번째 입력 : " % (count+1), end="")
        chk = input()

        if(chk.isnumeric() == True) :
            nums[count] = int(chk)
            count += 1
        else :
            print("숫자가 아닙니다. 숫자를 입력하세요.")
    while True :
        print("입력된 값을 어떻게 처리할까요?")
        print("1. 오름차순 정렬")
        print("2. 내림차순 정렬")
        print("3. 합계를 출력")
        print("4.합계를 리스트에 추가")
        print("5. 프로그램 종료")

        cmd = int(input("명령을 입력하세요 : "))
                  
        if (cmd == 1) :
            s_nums = sort(argc, *nums)
            print("오름차순정렬")
            print(s_nums)

#main 시작부분
                
print("List의 크기를 입력하세요 : ", end="")
size = int(input())

input_numbers(size)

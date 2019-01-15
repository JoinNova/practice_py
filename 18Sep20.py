#예외를 하면 종료되는데 예외가 발생하면 except절로 넘어가서 다시 해결하게만든다.
'''
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
            print("숫자가 아닙니다. 숫자를 입력하세요.")
    while True :
        print("입력된값을 어떻게 처리할까요?")
        print("1.리스트를 오름차순으로 정렬")
        print("2.리스트를 내림차순으로정렬")
        print("3.합계를출력")
        print("4.합계를 리스트에추가한것을출력")
        print("5.프로그램종료")

        print("명령을 입력하세요.", end="")
        cmd=int(input())

        if (cmd==1) :
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
            print("5.프로그램종료")
            import sys
            sys.exit()
            
##메인코드부분

if __name__ =='__main__' :
    try :

        print("List의 크기를 입력하세요 : ", end="")
        size=int(input())
        input_numbers(size)
    except :
        print("입력한값은 숫자가 아닙니다.")
    else:
        
        print("List의 크기를 입력하세요 : ", end="")
        size=int(input())
        input_numbers(size)
    finally:
        print("프로그램을종료합니다.")

my_list=[1,2,3]

try:
    print("첨자를 입력하세요.")
    index=int(input())
#    print(my_list[index]/0)
    print("my_list[{0}]:{1}".format(index, my_list[index]))


except Exception as err:
    print("1) 예외가 발생했습니다.({0})".format(err))
except ZeroDivisionError as err:
    print("2) 0으로 나눌수 없습니다.({0})".format(err))
except IndexError as err:
    print("3)잘못된 첨자입니다.({0})".format(err))
else:
    print("리스트이 요소 출력에 성공했습니다.")
finally:
    print("어떤 일이 있어도 마무리합니다.")

def some_function():
    print("1~10 사이의수를 입력하세요.")
    num=int(input())
    if num<1 or num>10:
        raise Exception("유효하지 않은 숫자입니다.:{0}".format(num))
    else:
        print("입력한 수는 {0}입니다.".format(num))
def some_function_caller():
    try:
        some_function()
    except Exception as err:
        print("1)예외가발생했습니다.{0}".format(err))
        raise
try:
    some_function_caller()
except Exception as err:
    print("2)예외가 발생했습니다.{0}".format(err))


class MyException(Exception):
    pass
class MyException(Exception):
    def __init__(self):
        super().__init__("MyException이 발생했습니다.")

'''
class InvalidIntException(Exception):
    def __init__(self,arg):
        super().__init__('정수가 아닙니다.:{0}'.format(arg))
def convert_to_integer(text):
    if text.isdigit():#부호(+,-)처리 못함.
        return int(text)
    else:
        raise InvalidIntException(text)
if __name__=='__main__':
    try:
        print('숫자를 입력하세요:')
        text=input()
        number=convert_to_integer(text)
    except InvalidIntException as err:
        print('예외가 발생했습니다({0})'.format(err))
    else:
        print('정수 형식으로 변환되었습니다: {0}{1}'.format(number,type(number)))

'''
###whals21
def solution(n):
    arr = [] 
    for i in range(1, n+1) :
        if n % i == 0 :
            arr.append(i)     
    if sum(arr) == n*2:
        return print("\n",n,"-yes","\n")     
    else:
        print("no",end='')
if __name__ =='__main__':
    for _ in range(10000):
        solution(_)
'''
'''
###nova
for _ in range(10000):
    n=_

    nl=0
    for i in range(1,n):
        if n%i==0:
            nl+=i
    if nl==n:
        print(n,'yes','\n')
    else:
        print('no',end='')
'''
'''
###채원
for _ in range(10000):
    a = _
    alist = [] 
    for i in range(1,a,1):
        if a%i == 0:
            alist.append(i)
        else:
            continue 
    if sum(alist) == a:
        print('\n',a,"yes\n") 
    else:
        print("no",end='')
'''
'''
###종철
for _ in range(10000):
    n = _
    c = 0 
    for i in range(1, n, 1) :
        if n%i == 0 :
            c += i 
    if c == n :
        print('\n',n,"yes\n")
    #elif n > 1000 :
        #print("1000을 초과한 수 입력")
    else :
        print("no",end='')
'''
'''
###ripta
def perfec_num(num):
    list = []
    list2 = []
    sum = 0
     
    for i in range(1, num+1):
        list.append(i)
        if num % list[i-1] == 0:
            list2.append(list[i-1])
    for j in range(len(list2)-1):
        sum += list2[j]     
    if sum == num:
        return "\nyes\n"
    else:
        return "no"                 
for _ in range (10000):
    num = _
    print(perfec_num(num),end='')
'''
'''
###진택______________X
n = int(input(" 수 : "))
nlist = []
 
for i in range(1,n):
    if n%i==0:
        nlist.append(i)
    else :
        continue
 
if sum(nlist) == n:
    print("\n%dyes\n"%n)
else:
    print("no",end='')
'''
'''
###Limks____________X
n=int(input())
temp=0
for i in range(1,n,1):
    if n%i==0:
        temp=temp+i
if temp==n:
    print(temp,'는 완전수입니다.')
'''
'''
###태균
def com(a):
    num = []
    for i in range(1, a + 1):
        if a % i == 0:
            num.append(i)
    return num
def whan(a):
    m = max(w)
    s = sum(w) - m
    if s == m:
        print(v,"True")
if __name__ == "__main__":
    for _ in range(1,10000):
        v = _
        w = com(v)
        whan(w)
'''

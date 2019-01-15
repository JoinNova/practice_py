'''
###태균___________O
def mid(a):
    r = 0
    for i in range(0, v):
        r += i
    return r
def yo(a):
    print(m)
    r = 0
    for i in range(v + 1, 10000000000000000):
        r += i
        if r >= m :
            return r
            break
def final(a, b):
    if m == y:
        print("이 숫자는 중간수 입니다.")
    else :
        print("이 숫자는 중간수가 아닙니다.")

if __name__ == "__main__":
    v = int(input("정수를 입력해주세요 : "))
    m = mid(v)
    y = yo(v)
    final(m,y)
'''

###nova________________O
n=int(input())
s=0
b=0
chk=0
s=sum(range(n))
print(s)
for i in range(n+1,s+1):
    
    b+=i
    if s==b:
        chk+=1
        print('O')
        break
if chk==0:
    print('X')

'''
###whals21________________O
def solution(n):
    f, b = 0, 0     
    for i in range(n):
        f += i
    for j in range(n+1, n*n):
        b += j
        if f == b:
            return print("O")
        elif f < b:
            return print("X")
if __name__ == '__main__':
    solution(int(input()))
'''
'''
###Limks__________X
n=int(input('n='))
sumi=0
sumk=0
for i in range(1,n,1):
    sumi=sumi+i
for k in range(1,n,1):
    if sumi>sumk:
        sumk+=(n+k)
    elif sumi == sumk:
        print(n,'는 중간수입니다.')
        break
    else:
        print(n,'는 그냥수입니다.')
        break
'''
'''
###종철_______________O
n = int(input("입력 : ")) 
l = 0
r = 0
m = 0 
if n <= 10000000 :
    for i in range(1, n, 1) :
        l += i 
    #r = (n+1)+(n+2)+...+(n+m)
    m = n+1
    while 1 :
        r += m
        m += 1
        if r == l :
            break
        elif l < r :
            break 
    if l == r :
        print("O")
    else :
        print("X") 
else :
    print("10000 이하의 자연수를 입력하시오.\n현재 입력한 수 : %d" % n)
'''
'''
###채원____________O
a = int(input("숫자입력"))
b=1
for i in range(1,a-1,1):
    b+=i+1
c=0
k=a+1
while b > k:
    c += 1   
    k += a+(c+1)
if b==k:
    print("O")
else :
    print("X")
'''

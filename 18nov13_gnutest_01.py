
'''
n=int(input())
chk2=0
for i in range(1,1000000000):
    k=str(i)
    chk1=0
    for j in range(len(str(i))):
        if k[j]=='4' or k[j]=='7':
            chk1+=1
    if chk1==len(str(i)):
        chk2+=1
    if chk2==n:
        print(i)
        break
'''

def solution(a):
    a = int(a)
    if a < 1:
        return ''
    solution((a-1)/2)
    if a%2 == 0:
        print('7', end='')
    else:
        print('4', end='')
solution(int(input()))


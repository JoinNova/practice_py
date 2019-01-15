'''
import re
def function(alpha) : 
    if alpha.islower():
        return ord(alpha)-97  #from a(0) to z(25) 
    elif alpha.isupper():
        return ord(alpha)-65+(26)  #from A(26)  to Z(51)
    else:
        return ord(alpha)-48+(52)   #from 0(52)  to 9(61)
x=input()
y=list(x)
k=0
y=sorted(y,key=function)
A = str(y)
B = A.split('S')
print(B)
C = re.findall("[0-9]+", A)
print(C)
for i in range (0, len(C)-1, 1):
    if (int(C[i]))%2==0 :
        if (int(C[i]))<(int(C[i+1])):
            k=C[i]
            C[i]=C[i+1]
            C[i+1]=k
print(C)



for i in range (0, len(x), 1):
    print(y[i], end="")
    
'''

myList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
print(*sorted(input(), key = myList.index), sep ="")

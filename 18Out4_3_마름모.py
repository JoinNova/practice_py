#마름모그리기
a=int(input("그리고 싶은 최대 마름모 가로길이 별의 갯수는??? : "))
b=a

for a in range(1,a,2):
    print(" "*int((b-a)/2),"*"*a)

for a in range(a+2,0,-2):
    print(" "*int((b-a)/2),"*"*a)

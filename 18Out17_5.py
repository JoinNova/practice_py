if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    a=[]
    b=[]
    for i in range(0,x+1,1):
        for j in range(0,y+1,1):
            for k in range(0,z+1,1):
                a=[]
                a.append(i)
                a.append(j)
                a.append(k)
                if (i+j+k)!=n:
                    b.append(list(a))

    print(b)

import textwrap
def wrap(string, max_width):
    a=[]
    c=[]
    count=0
    d=max_width
    for i in range (0,len(string),1):
        count+=1
        a.append(string[i])
        if count%d==0 :
            c.append(a)
            a=[]
        elif i==(len(string)-1):
            c.append(a)

    return c
if __name__=='__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

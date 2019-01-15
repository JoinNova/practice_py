def fun(s):
    import re
    try:
        result=False
        regex_pattern = r"[@.]"
        chk=re.split(regex_pattern,s)
        if len(chk)==3:
            print(chk)
            chk22=0
            for i in range(3):
                if i==0:
                    if chk[0]=='':
                        chk22+=1
                    for j in range(len(chk[0])):
                        regex_pattern = r"[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\-_]"
                        chk2=re.split(regex_pattern,chk[0])
                        for j in range(len(chk2)):
                            if len(chk2[j])!=0:
                                chk22+=1#chk22=0선언해야함
                elif i==1:
                    for j in range(len(chk[1])):
                        regex_pattern = r"[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789]"
                        chk2=re.split(regex_pattern,chk[1])
                        for j in range(len(chk2)):
                            if len(chk2[j])!=0:
                                chk22+=1#chk22=0선언해야함
                else :
                    if len(chk[2])>3:
                        chk22+=1
                    for j in range(len(chk[2])):
                        regex_pattern = r"[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789]"
                        chk2=re.split(regex_pattern,chk[1])
                        for j in range(len(chk2)):
                            if len(chk2[j])!=0:
                                chk22+=1#chk22=0선언해야함
        if chk22==0:
            result=True
        return result           
                    
    except:
        result=False
    return result

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

x=0

y=0

sosoo=int(input('어디까지의 소수를 구해드릴까요?'))



for x in range (2,sosoo+1,1):

    count = 0

    for y in range(2,x+1,1):

        if x%y == 0:

            count+=1

            

    if count == 1:

        print(x)

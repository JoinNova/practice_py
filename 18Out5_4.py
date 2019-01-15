'''
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
'''
nums=[]
for i in range(2,101,1):
    nums.append(i)
print(nums)
namerge=[]

for i in range(0,100,1):
    count=0
    for j in range(2,101,1):
        if (nums[i]%j)==0:
            count+=1
    namerge.append(count)
print(namerge)

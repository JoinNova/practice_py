OneToHundred=[]
CompositeNumber=[]
 
for i in range(1, 101, 1):
      OneToHundred.append(i)
 
for i in range(1, 101, 1):
      for j in range(1,101,1):
            for k in range(1,101,1):
                  if i==j*k and j!=1 and k!=1:
                        CompositeNumber.append(i)
                         
OneToHundred_list = set(OneToHundred)
CompositeNumber_list = set(CompositeNumber)
PrimeNumber=OneToHundred_list.difference(CompositeNumber_list)
print(PrimeNumber)

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the time_delta function below.
def time_delta(t1, t2):
    from dateutil.parser import parse
    from dateutil.relativedelta import relativedelta
    t11=parse(t1[:24])
    h1=int(t1[26:28])
    m1=int(t1[28:])
    tt1=h1*3600+m1*60
    if t1[25]=='-':
        tt1=-tt1
    t22=parse(t2[:24])
    h2=int(t2[26:28])
    m2=int(t2[28:])
    tt2=h2*3600+m2*60
    if t2[25]=='-':
        tt2=-tt2
    gap=t22-t11
    gap2=tt2-tt1
    print(-gap)
    if gap.total_seconds()<0:
        gap=-gap
    result=datetime.second(gap.total_seconds())+gap2
    return result

    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(type(delta))
        print(delta)
        #fptr.write(delta + '\n')
    #fptr.close()

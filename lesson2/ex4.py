# s=101998//100000
# s=(101998%100000)//10000
# s=((101998%100000)%10000)//1000
# s=(((101998%100000)%10000)%1000)//100
# s=((((101998%100000)%10000)%1000)%100)//10
# s=(((((101998%100000)%10000)%1000)%100)%10)//1
# s1 = 101998//10
# s2 = 101998%10
# x1 = 101998//1000
# x2 = ((101998%1000)%10 )
# print(x1, x2)
# a=int(input())
# b=int(input())
#
# [a,b,c] = [c,b,a]
#
#
# print(a,b)
import math
import random
for i in range(100):
    print(random.random())
    print(random.randint(0,10000))
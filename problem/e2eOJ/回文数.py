'''x=input()
y=[]
for i in x:
    y.append(i)
z=y[::-1]
if z==y:
    print('true')
else:
    print('false')'''
import turtle

'''class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        y=[]
        for i in x:
            y.append(i)
        z=y[::-1]
        if z==y:
            return True
        else:
            return False'''
'''import turtle
a=60
turtle.forward(a)
turtle.left(120)
turtle.forward(a)
turtle.left(120)
turtle.forward(a)
turtle.left(120)'''

'''for i in range(10000000000):
    print()'''

# def isPowerOfThree(n: int):
#         import numpy
#         x=numpy.log(n)/
#         if n>0:
#             if n==3**int(x):
#                 return True
#             else:
#                 return False
#         else:
#             return False
# print(isPowerOfThree(177147))

# import numpy
# print(numpy.log(3))
# import math
# print(round(math.log(243,3),10))
# a, b, c = int(input("请输入a:")), int(input("请输入b:")), int(input("请输入c:"));der = b * b - 4 * a * c;x1 = (der ** 0.5 - b) / 2 * a;x2 = (der ** 0.5 + b) / 2 * a;d = "无实根" if der <= 0 else "两个实根分别为: " + str(x1) + " " + str(x2);print(d, x1, x2)

# c=0
# for i in range(100,201):
#     if i%3 ==0 and i&7 ==0:
#         pass
#     else:
#         c+=i
# print(c)

# x,y=int(input()),int(input());print((x+y)*(x-y+1)*0.5)
# def mySum(x,y):
#     sum=(x+y)*(y-x+1)*0.5
#     return sum
# x=int(input())
# y=int(input())
# sum=mySum(x,y)
# print(sum)

"""def mySum(x,y):
    sum=int((x+y)*(y-x+1)*0.5)
    return sum
x=int(input())
y=int(input())
sum=mySum(x,y)
print(sum)"""
'''s=input("score:")
if s<="9":
    s=int(s)
    if  s>=90: grade="优"
    elif  s>=80: grade="良"
    elif  s>=70: grade="中"
    elif  s>=60: grade="及格"
    else:  grade="你不及格！请注意补考通知！"
    print("grade:",grade)
else:
    print("输入有误！")'''
'''a = [0, 1, 0]
print(len(a))
rowIndex=3

for i in range(1, rowIndex + 1):
    b = [0, 0]
    for i in range(0, len(a)-1):
        x=i
        c = a[x] + a[x+1]
        b.insert(i+1,c)
    a=b
del a[0]
del a[len(a)-1]
print(a)'''
'''def isBadVersion(aa):
    e=10
    if aa<e:
        return False
    else:
        return True
n=15
top, base = n, 0

while 1:
    temp = int(round(base / 2 + top / 2, 0))
    if isBadVersion(temp) == bool(1):
        top = int(round(base / 2 + top / 2, 0))
    elif isBadVersion(top) == bool(1) and isBadVersion(top - 1) == bool(0):
        print(top)
        break
    else:
        base = int(round(base / 2 + top / 2, 0))'''


# a=input
#
# a=2**31-1;c=1
# while a>0:
#
#     a,c=a//2-1,c+1
# # print(c)
# d=""
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(j,i,i*j),end=" ")
#         d+=
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,'*',i,'=',i*j,sep='',end=' ')
#     print()

# for i in range(1,1001):
#     print(i/17)
#     if i/17 == 0:
#         print(i,end=" ")
#     else:
#         pass

#
# def fibo(a):
#     for i in range(1,a+1):
#         b,c,d=1,1,1;b=c+d;c,d=b,c
#     return b
# n=int(input("请输入n(n>=1):"))
# for i in range(1,n+1):
#     print(fibo(i),end=' ')


# a=input("请输入一个三位数的整数:");b="百十千"
# for i in range(0,3):
#     print("%s位:%s"%(b[i],a[i]))

# n=int(input());print(sum(list(range(1,n+1,n))))
# h=int(input("请输入球落下的高度:"));S=2*(1023/1024))*h;Hn=h*(1/1024);print("共经过距离%f米"%S);print("第10次反弹%f米"%Hn)

# import math
# from decimal import *
# print(1.0+2.0)
#
# def my_pow(x, y, prec, modulo=None):
#     a = Decimal(x)
#     b = Decimal(y)
#     getcontext().prec = prec
#     if not modulo:
#         c = Decimal(modulo)
#     return pow(a, b, c)
#
#
# from fractions import Fraction
#
#
# def asd(n):
#     return math.pow(math.sin(Fraction(3,3 ** n)), Fraction(1,n))
#
#
# for i in range(1, 10000):
#     print(asd(i))


# import math as m
# def s(n:int) -> float:
#     return m.sin(1/m.pow(3,n))
#
#
# def m(n:int) -> f

# def ab (a:int):
#     turtle.forward(a)
#     turtle.left(120)
# import turtle
#
# a=40
# ab(a);ab(a);ab(a)

# s=0
# list1=[1,2,3,4, 5,6,7,8,9,10]
# for i in list1:
#     s+=i
# print(i)
# for a in [i]:
#     print(a)

#
# if __name__ == "__main__":
#     print(f"测试")
#
#
# def asd():
#     print("测试2")
#
#
# # tensor=torch.rand(3,4)
# print(f"Shape of tensor:{1+1}")
# # 这条语句等效于
# print("Shape of tensor:{}".format(1+1))


# def f(x, y: float = 0, z=0) -> int:
#     return 0
#     print(x, y, z)



# zhan=[]
import math


def j(d):
    a=1
    for i in range(1,d+1):
       a*=i
    return a

# print(j(5))
#
# n=1
# b=0
# while 1:
#     b+=(math.pow(-1,n-1)*math.pow(2,n*n))/j(n)
#     print(b)
#     n+=1
__e=1
n=1
while round(__e,14)!=round(math.e,15):
    __e+=1/j(n)
    n+=1
    print(__e,math.e)
# def login(user,password):
#     with open('cookic.txt', 'r', encoding='utf-8') as f:
#         usertmep = {}
#
# user = input("请输入用户名：")
# password = input("请输入密码：")


# m=1
# for x in range(1,4):
#       m*=x
# print(m,sep='')

# a= 5
# b= 6
# c= 7
# print(pow(b,2) - 4*a*c)
#
# from math import *
# import math
# sqrt(1234132)


# a=1
# b = 1.0
# s = 0
# for n in range(1,4):
#     s += a/ b
#     t = a
#     a= a+ b
#     b= t


# sum=0
# for i in range(10,25):
#     if i%5==0:
#          sum+=i
# print(sum,i)

# def fan(v):
#     return int(not bool(v))
#
# print(fan(0))


# class Solution:
#     def destCity(self, paths) -> str:
#         def fan(v):
#             return int(not bool(v))
#
#         def end(path, n):
#             if path in paths[n + 1]:
#                 return paths[n + 1][fan(paths[n + 1].index(path))]
#             else:
#                 end(paths[n][fan(paths[n].index(path))], n)
#
#         n = 0
#         path = paths[0][0]
#         while n < len(paths):
#             path = end(path, n)
#             n += 1
#         else:
#             return path
#
#
# paths=[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# m=Solution.destCity(paths)
# print(m)

# def func(num):
#     num*=2
#     return num
# x=20
# x=func(x)
# print(x)

# for a in 'mirror':
#     print(a, end="")
#     if a == 'r':
#         break


# print(type(3//2.0))\



try:
    a=int(input(""))
    print(a * 5)
except:
    print("请输入整数")

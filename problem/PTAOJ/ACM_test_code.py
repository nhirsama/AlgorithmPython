# n = input()
# n+=", Start"
# print(n)

# t = input().split()
# h = int(t[1])
# t = int(t[0])
# if t<0:
#     print("Wear a thick coat to keep warm!")
# elif t<20:
#     if h>80:
#         print("Suggest wearing a raincoat.")
#     else:
#         print("Suggest wearing long sleeved shirts.")
# elif t<30:
#     print("Suitable for wearing short sleeves.")
# else:
#     print("Wear lightweight clothing.")

# def ThereToTen(There):
#     a = 0
#     return int(There[0])*3**2+int(There[1])*3**1+int(There[2])
# n = input()
# def printChar(There):
#     a = ThereToTen(There)
#     if a == 0:
#         print(" ",sep="",end="")
#     else:
#         print("%c"%(a+100-4),sep="",end="")
# for i in range(0,len(n),3):
#     printChar(n[i:i+3])

# t = int(input())
# line=[]
# for i in range(t):
#     n = input().split()
#     n[0] = int(n[0])
#     n[1] = int(n[1])
#     line.append(n)
# max = max(line)[0]
# char = [1]
# for i in range(max-1):
#     char2 = char.copy()
#     for j in range(len(char2)):
#         char2[j] = char2[j]*2
#     char = char2 + char +char2
# lenchar = len(char)
# for i in range(t):
#     hangstart = 0
#     if line[i][0] == 0:
#         hangstart = 0
#     else:
#         hangstart = int(lenchar/3**(line[i][0]-1))
#     print(char[hangstart+int(line[i][1])-2]%998244353)

# n,c = input().split()
# n = int(n)
# c = int(c)
# a = []
# for i in range(int(n)):
#     a.append(input().split())
# toC,money = 0,0
# while True:
#     if toC >= c:
#         break
#     temp = 0
#     jiaobiao = 0
#     if a == []:
#         money = "Error!"
#         break
#     for i in range(len(a)):
#         aaa = int(a[i][1])/int(a[i][0])
#         if aaa>temp:
#             temp = aaa
#             jiaobiao = i
#         else:pass
#     for i in range(2):
#         if toC < c:
#             toC += int(a[jiaobiao][0])
#             money += int(a[jiaobiao][1])
#         else:
#             break
#     else:
#         a.pop(jiaobiao)
# print(money)

# n,m = input().split()
# n = int(n)
# m = int(m)
# yiji = 1
# def toyiji(tov,yiji,n):
#     if yiji+tov >= n:
#         yiji+=tov-n
#         return yiji
#     else:
#         yiji+=tov
#         return yiji
# str = input().split()
# tov=1
# for i in str:
#     if i =="1":
#         yiji = toyiji(tov,yiji,n)
#     elif i =="2":
#         tov+=1
#     else:
#         print(yiji)

# n = int(input())
# for i in range(2000000000):
#     for j in range(i):
#         for k in range(j):
#             if 2*i*j*k/(j*k+i*k+i*j) == n:
#                 print(k, j, i)
#                 break
# else:print(-1)


# n,k = input().split()
# n = int(n)
# k = int(k)
# piont = input().split()
# i = 1
# day = 0
# sum =0
# sum2 = 0
# for j in range(1,10):
#     i=j
#     while i < n:
#
#         if day >= 3:
#             break
#         if int(piont[i-1])>int(piont[i]):
#             day+=1
#
#             sum+=int(piont[i-1])
#             i += 1
#         i += 1
#     if sum2< sum:
#         sum2 = sum
# print(sum)


# t = int(input())
# line=[]
# for i in range(t):
#     n = input().split()
#     n[0] = int(n[0])
#     n[1] = int(n[1])
#     line.append(n)
# max = max(line)[0]
# char = [1]
# for i in range(max-1):
#     char2 = char.copy()
#     for j in range(len(char2)):
#         char2[j] = char2[j]*2
#     char = char2 + char +char2
# lenchar = len(char)
# for i in range(t):
#     hangstart = 0
#     if line[i][0] == 0:
#         hangstart = 0
#     else:
#         hangstart = int(lenchar/3**(line[i][0]-1))
#     print(char[hangstart+int(line[i][1])-2]%998244353)

# t = int(input())
# line = []
# for i in range(t):
#     n = input().split()
#     n[0] = int(n[0])
#     n[1] = int(n[1])
#     line.append(n)
# # max = max(line)[0]
# char = [1]
# for m in line:
#     char = [1]
#     for i in range(int(m[0]) - 1):
#         char2 = char.copy()
#         for j in range(len(char2)):
#             char2[j] = char2[j] * 2
#         char = char2 + char + char2
#
#     aaa = int(m[1])-1
#     print(char[aaa])


n = int(input())
for i in range(120):
    for j in range(i):
        for k in range(j):
            if 2*i*j*k/(j*k+i*k+i*j) == n:
                print(k, j, i)
else:print(-1)
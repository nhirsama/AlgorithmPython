
"""
def minlen(word1, word2):
    if len(word1) > len(word2):
        return word2
    else:
        return word1

def maxlen(word1, word2):
    if len(word1) > len(word2):
        return word1
    else:
        return word2

def mergeAlternately(word1, word2):
    word3 = ""
    for i in range(0, len(minlen(word1, word2))):
        word3 += word1[i] + word2[i]
    else:
        word4 = minlen(word1, word2)
        word3 += maxlen(word1, word2)[i+1:len(maxlen(word1, word2))]
        return word3
"""
from os.path import split

''' 力扣1768题，交替合并字符串
if __name__ == '__main__':
    word1 = "abcd"
    word2 = "pqr"
    print(mergeAlternately(word1, word2))
'''
"""     #洛谷的题，这个算法时间复杂度太高了，在C里面有o（n）的算法
def tiaohe(n,sn=0):
    if n==1:
        return 1
    sn+=1/n + tiaohe(n-1,sn)
    return sn


a = int(input())
n = 1
while a>=tiaohe(n):
    n+=1
print(n)
"""
"""------------------------------------------------------------"""


"""------------------------------------------------------------"""
"""     #洛谷P1089题 
def tongji(a):
    qian = 0
    zhan = []
    for i in range(1, 13):
        qian += 300
        qian -= a[i - 1]
        if qian < 0: return -i
        else:
            zhan.append(qian//100)
            qian = qian%100
    return sum(zhan)*120+qian

a = []

for i in range(12):
    a.append(int(input()))
print(tongji(a))

"""
"""------------------------------------------------------------"""


"""------------------------------------------------------------"""
"""     #洛谷题，感觉很不好评价
a,b,c = 0,0,0
str =input()
str = str.replace(':','')
# for i in range(3):
#     str2 = str.split(";")
# for i in range(3):
#     str2[i] = str2[i][0]+str2[i][2:4]
exec(str)
print(a,b,c)
"""
"""------------------------------------------------------------"""


"""------------------------------------------------------------"""
"""     #洛谷P1015题，其中N应为进制数，本程序理解为限制迭代次数。
a = int(input())
N = int(input())
m = 0
while m<=N:
    if a==int(str(a)[::-1]):
        break
    else:
        a = a+int(str(a)[::-1])
        m+=1

if m>N:
    print("Impossible!")
else:
    print("STEP=",m,sep="")
"""
"""------------------------------------------------------------"""


"""------------------------------------------------------------"""
"""     #P1720 月落乌啼算钱（斐波那契数列）
import math
n = int(input())
sqrt5 = math.sqrt(5)

fn = (pow((1+sqrt5)*0.5,n)-pow((1-sqrt5)*0.5,n))/sqrt5
print("%.2f"%fn)
"""
"""------------------------------------------------------------"""


"""------------------------------------------------------------"""
"""     #P1401 [入门赛 #18] 禁止在 int 乘 int 时不开 long long
        #不好评价，这个代码101和102的代码wa，写不明白为什么
import math
temp = input()
temp = temp.split(" ")
xl,xu = int(temp[0]),int(temp[1])
temp = input()
temp = temp.split(" ")
yl,yu = int(temp[0]),int(temp[1])
if xl<0:
    xl = -xl
if yl<0:
    yl = -yl
if (xu == 0 and xl == 0) or (yu == 0 and yl == 0):
    xl = 1
    yl = 1
xu,yu = math.log(max(xl,xu),2,),math.log(max(yl,yu),2)
if xu+yu>31:
    print("long long int")
else:
    print("int")
"""

"""------------------------------------------------------------"""


"""------------------------------------------------------------"""
"""
#力扣 2511题，懒得写了。
forts = [0,0,1,-1]
# while True:
#     if forts == []:
#         return 0
#     elif forts[-1] == 1:
#         forts.pop()
#         break
#     else:
#         forts.pop()
# while True:
#     if forts == []:
#         return 0
#     elif forts[0] == 1:
#         forts.pop(0)
#         break
#     else:
#         forts.pop(0)

while True:
    if forts[0] == 0:
        forts.pop(0)
    else:
        break
a = 0
b=[]
for i in forts:
    if i == 0:
        a+=1
    if i == -1 or i == 1:
        b.append(a)
        a = 0
b.append(a)
a = max(b)
print(a)
"""

"""------------------------------------------------------------"""


"""------------------------------------------------------------"""


# # [BalkanOI2003] Farey 序列
#
# ## 题目描述
#
# 把所有分子和分母都 $\leq n$ 的**最简真分数**从小到大排成一行，形成的序列称为 Farey 序列。
#
# 求出 $n$ 所对应的 Farey 序列中第 $k$ 小的数。
#
# ## 输入格式
#
# 一行，两个整数 $n, k$。
#
# ## 输出格式
#
# 一行，两个整数 $p, q$，表示答案 $\frac{p}{q}$。
#
# ## 样例 #1
#
# ### 样例输入 #1
#
# ```
# 5 6
# ```
#
# ### 样例输出 #1
#
# ```
# 3 5
# ```
#
# ## 提示
#
# 对于 $100\%$ 的数据，$2 \leq n \leq 4 \times 10^4$，$1 \leq k \leq$ 符合条件的分数的个数。
"""     #虽然写的确实没问题，但是时间复杂度相当高，对于n = 5000的数据占了快一个G内存，跑了两分钟以上。
n = input().split()
q = int(n[1])
n = int(n[0])
Farey = []
door = q/n
def asdf(elem):
    return elem[0]/elem[1]
for i in range(n+1):
    for j in range(1,min(i+1,q)):
        if i == j:
            break
        if i%2 == 0 and j%2 == 0:
            break
        if j/i >= door:
            break
        Farey.append([j,i])
print(Farey)
Farey.sort(key=asdf)
print(Farey)
k = 0
while k<=len(Farey)-1:
    if asdf(Farey[k]) == asdf(Farey[k-1]):
        Farey.pop(k)
    else:
        k+=1
print(Farey)
print(Farey[q-1][0],Farey[q-1][1])

"""
"""------------------------------------------------------------"""


"""------------------------------------------------------------"""
"""
def aaa(a = 0,b = 0,c = []):
    print(a,b,c)

if __name__ == '__main__':
    a1,b2 = 5,334
    c = [123]
    aaa(a1)
    aaa(b = b2)
    aaa(c = c)
    aaa(a1,c = c)
"""

"""
def 阶乘(n):
    if n==1:
        return 1
    return n*阶乘(n-1)

if __name__ == '__main__':
    n = int(input())
    print(阶乘(n))
"""
'''#打印一个九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}x{i}={i*j}", end="\t")
    print()
'''
# names = ['Li', 'Zhang', 'Wang', 'Zhang', 'Li', 'Wang', 'Li', 'Wang', 'Wang']
# d = {'Li': 0, 'Zhang': 0, 'Wang': 0}
# for i in names:
#     d[i] +=1
# print(d)

'''names = ['Li', 'Zhang', 'Wang', 'Zhang', 'Li', 'Wang', 'Li', 'Wang', 'Wang'];d = {'Li': 0, 'Zhang': 0, 'Wang': 0};
i = name[1]
d[i] += 1
i = name[2]
d[i] += 1
i = name[3]
d[i] += 1
i = name[4]
d[i] += 1
i = name[5]
d[i] += 1
i = name[6]
d[i] += 1
i = name[7]
d[i] += 1
i = name[8]
d[i] += 1
i = name[9]
d[i] += 1
# print(d)'''
# for i in range(0,10):
#     print("d[",i,sep="",end="")
#     print("] +=1",sep="",end=";")
#     print("d[i] += 1",sep=";",end=";")
# names = ['Li', 'Zhang', 'Wang', 'Zhang', 'Li', 'Wang', 'Li', 'Wang', 'Wang'];d = {'Li': 0, 'Zhang': 0, 'Wang': 0};d[1] +=1;d[2] +=1;d[3] +=1;d[4] +=1;d[5] +=1;d[6] +=1;d[7] +=1;d[8] +=1;d[0] +=1;print(d)
#for语句使用分号编写在同一行后会报错,得想个别的办法.本题收获，在F12使用控制台禁用JavaScript可粘贴代码，在python中使用for循环与sep、end参数可批量输出代码。
# for i in names:
#     print("d['%s'] += 1"%i,end=";")
# names = ['Li', 'Zhang', 'Wang', 'Zhang', 'Li', 'Wang', 'Li', 'Wang', 'Wang'];d = {'Li': 0, 'Zhang': 0, 'Wang': 0};d[Li] += 1;d[Zhang] += 1;d[Wang] += 1;d[Zhang] += 1;d[Li] += 1;d[Wang] += 1;d[Li] += 1;d[Wang] += 1;d[Wang] += 1;print(d) #for语句使用分号编写在同一行后会报错,得想个别的办法.本题收获，在F12使用控制台禁用JavaScript可粘贴代码，在python中使用for循环与sep、end参数可批量输出代码.
from math import *

r = float(input())
h = float(input())
V = 1 / 3 * pi * r * r * h
L = (r * r + h * h) ** 0.5
S = pi * r * L + pi * r ** 2
print("V:%.2f" % V)
print("S:%.2f" % S)

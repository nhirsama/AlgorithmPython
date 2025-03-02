#     #循环输出1-9的每个数字，重复9次
# aaa = 9
# while aaa != 0:
#     for i in range(1, 10):
#         print(i,end='')
#     aaa = aaa-1
#     print()

# 循环算法打印九九乘法表
i = int()
j = int()
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%u*%u=%u ' % (i, j, i*j), end='')
    print()

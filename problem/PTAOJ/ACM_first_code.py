#此main文件为acm校内预选拔赛调试环境用文件

#力扣283题解
"""
nums = eval(input())
i = 0
j = len(nums)
while i < len(nums):
    if nums[i] == 0:
        nums.pop(i)
    else:i+=1
for i in range(0,j-len(nums)):
    nums.append(0)
print(nums)
"""


#力扣66题 加一
"""
digits = [1,2,4,5,6,7,2,1]
a = ""
for i in digits:
    a = a + str(i)
a = int(a) + 1
a = str(a)
b = []
for i in list(a):
    b.append(int(i))
print(b)
"""

#力扣1822 数组元素积的符号
#优化方法，选出数组最小的两个元素，求差获得公差，对数组累加，判断数组之和
#是否满足等差数列的前n项和公式。

"""
arr = [1,2,4]
arr.sort()
asdf = True
for i in range(1,len(arr)-1):
    if 2*arr[i] == arr[i+1]+arr[i-1] and asdf:
        pass
    else:
        asdf = False
print(asdf)
"""

#力扣 896单调数列
#这题挺简单的，实际上只要判断每一项的前一个值和这一项的大小关系就行
#一开始想复杂了
"""
nums = [1,3,2]
nums2 = nums.copy()
nums2.sort()
if nums == nums2:
    print("True")
elif nums == nums2[::-1]:
    print("True")
else:
    print("False")
"""




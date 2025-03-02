# a=[1,2,3,4,5,6,7,8]
# print(a)
# print(a[4:1:-1])
# b=[i for i in range(0,5)]
# pr
# a= b= c=123
# print(a,b,c)


# print("a"<"b")
# print("cc">"cb")
#
#用于将1234转换为对应的ABCD
def abcd(a):
    if a=="1":
        return "A"
    if a=="2":
        return "B"
    if a=="3":
        return "C"
    if a=="4":
        return "D"

b=0
a="121212412241112231141142231213323"
for i in a:
    b+=1
    print(b,":",abcd(i))
#
#
#
# str1 = "mysqlsqlserverPostgresQL"
# str2 = "sql"
# ncount = str1.count(str2,10)
# print(ncount)


# X=y=z=m=n=5

#
# i=j=[]
# i.append(1)
# print(i,j)
#
#
# i=[1]
# j=i
# j.append(2)
# print(i)
#
# a="Hebeu"*2
# print(a[5:8])
#
# print(0.1+0.2)
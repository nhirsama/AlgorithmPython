inp = input().split()
n = int(inp[0])
k = int(inp[1])
ans = ((1+k)*k)//2
inp = input().split()
inp = set(inp)
for i in inp:
    if int(i)>k:
        continue
    ans-=int(i)
print(ans)


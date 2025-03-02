#此为AI生成代码，仅用于测试AI能力
def multiply(a, b, mod):
    res = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                res[i][j] += a[i][k] * b[k][j]
                res[i][j] %= mod
    return res

def matrix_pow(mat, power, mod):
    result = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    while power > 0:
        if power % 2 == 1:
            result = multiply(result, mat, mod)
        mat = multiply(mat, mat, mod)
        power //= 2
    return result

n, m = map(int, input().split())

if m == 1:
    print(0)
    exit()

res = 0
k = 1

while True:
    a = 10 ** (k - 1)
    if a > n:
        break
    b = min(10 ** k - 1, n)
    t = b - a + 1
    p = pow(10, k, m)
    mat = [
        [p, 1, 0],
        [0, 1, 1],
        [0, 0, 1]
    ]
    mat_pow = matrix_pow(mat, t, m)
    res = (res * mat_pow[0][0] + a * mat_pow[0][1] + mat_pow[0][2]) % m
    k += 1

print(res % m)
import sys

MOD = 10 ** 9 + 7
max_n = 2 * 10 ** 6

# 预处理阶乘和逆元阶乘
fact = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact = [1] * (max_n + 1)
inv_fact[max_n] = pow(fact[max_n], MOD - 2, MOD)
for i in range(max_n - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD


def comb(a, b):
    if a < 0 or b < 0 or a < b:
        return 0
    return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD


def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        n = int(input[idx])
        m = int(input[idx + 1])
        idx += 2

        if n == 0 and m == 0:
            print(1)
            continue

        s = n + m
        base = comb(s, n)
        sum_adj = 0
        if n > 0 and m > 0:
            a = s - 2
            b = n - 1
            c = comb(a, b)
            sum_adj = (2 * (s - 1) % MOD) * c % MOD

        ans = (base + sum_adj) % MOD
        print(ans)


if __name__ == "__main__":
    main()
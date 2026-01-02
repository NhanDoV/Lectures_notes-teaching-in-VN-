MOD = 10**9 + 7

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_factorial(n, mod):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % mod
    return fact

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None
    return (x % m + m) % m

def mod_binom(n, k, mod, fact):
    if k < 0 or k > n:
        return 0
    inv_k = mod_inverse(fact[k], mod)
    inv_nk = mod_inverse(fact[n - k], mod)
    return fact[n] * inv_k % mod * inv_nk % mod

# Precompute cho n<=10^6
fact = mod_factorial(1000000, MOD)
print(mod_binom(1000000, 500000, MOD, fact))

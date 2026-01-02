def sieve(n):
    if n < 2:
        return []
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            # đánh dấu bội số p*p, p*(p+1), ...
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1

    # Lấy ra danh sách số nguyên tố
    for num in range(2, n + 1):
        if is_prime[num]:
            primes.append(num)
    return primes

# Ví dụ test
if __name__ == "__main__":
    limit = int(input('input an integer limit : '))
    print(f"Primes up to {limit}: {sieve(limit)}")
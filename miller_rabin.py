import random

def is_prime_miller_rabin(n, k=40):
    """
    Probabilistic test for primality. 
    n: number to test, k: number of tests (accuracy increases with k)
    """
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # Efficient modular exponentiation
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Test it
p = 104729
print(f"Is {p} prime? {is_prime_miller_rabin(p)}")
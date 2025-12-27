import random

def is_prime_miller_rabin(n, k=40, verbose=False):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False

    # Preprocessing: n-1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    if verbose:
        print(f"\n--- Testing n = {n} ---")
        print(f"Decomposition: {n}-1 = 2^{r} * {d}")

    for i in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if verbose:
            print(f"\nRound {i+1}: Testing base a = {a}")
            print(f"  Initial check: {a}^{d} mod {n} = {x}")

        if x == 1 or x == n - 1:
            if verbose: print("  Result: Probable prime (Initial match)")
            continue
            
        # The Squaring Loop
        composite_found = True
        for s in range(r - 1):
            x = pow(x, 2, n)
            if verbose: print(f"  Squaring step {s+1}: x = {x}")
            
            if x == n - 1:
                if verbose: print("  Result: Probable prime (Hit n-1)")
                composite_found = False
                break
        
        if composite_found:
            if verbose: print(f"  Result: Definitely COMPOSITE (Witness a={a})")
            return False

    return True






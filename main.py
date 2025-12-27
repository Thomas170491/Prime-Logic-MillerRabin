from src import is_prime_miller_rabin
import time

def run_test_suite():
    # Test cases: { Number: Expected_Result }
    test_cases = {
        2: True,
        13: True,
        17: True,
        561: False,   # Carmichael Number (The "Math Trap")
        1105: False,  # Another Carmichael Number
        104729: True, # 10,000th Prime
        104730: False # Even number
    }

    print("--- Miller-Rabin Test Suite ---")
    
    for n, expected in test_cases.items():
        start_time = time.time()
        result = is_prime_miller_rabin(n, k=40)
        end_time = time.time()
        
        status = "PASS" if result == expected else "FAIL"
        print(f"Testing {n:<8} | Expected: {str(expected):<5} | Got: {str(result):<5} | [{status}] ({end_time-start_time:.6f}s)")

if __name__ == "__main__":
    run_test_suite()
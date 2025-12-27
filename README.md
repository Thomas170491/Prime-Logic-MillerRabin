Miller-Rabin Primality Test Implementation
Project Overview

This repository contains a Python implementation of the Miller-Rabin primality test. As a Master of Mathematics, I developed this project to demonstrate the practical application of number theory in modern cryptography. This algorithm is a cornerstone of public-key cryptography, used globally to generate the large prime numbers required for RSA and Elliptic Curve Cryptography (ECC).
The Mathematics

The Miller-Rabin test is a probabilistic primality test based on the properties of strong pseudoprimes. It relies on two main mathematical pillars:

    Fermat's Little Theorem: If p is prime, then for any integer a, ap−1≡1(modp).

    Square Roots of Unity: In a field Zp​, the only solutions to x2≡1(modp) are x≡1 and x≡−1.

Algorithm Logic

To test an odd integer n>3:

    Find r and d such that n−1=2r⋅d (where d is odd).

    Choose a random witness a in the range [2,n−2].

    Compute x=ad(modn).

    If x=1 or x=n−1, n is a "probable prime."

    Otherwise, square x repeatedly (r−1 times). If x ever becomes n−1, n is a "probable prime."

    If neither condition is met, n is composite.

Technical Features

    Efficiency: Uses Python's internal pow(a, d, n) for modular exponentiation, ensuring O(klog3n) time complexity.

    Accuracy: By performing k independent trials, the probability of a composite number being identified as prime is less than 4−k. With the default k=40, the error margin is negligible.

    Robustness: Designed to identify Carmichael numbers (composite numbers that pass the standard Fermat primality test).

Installation and Usage
Requirements

    Python 3.x

Setup
Bash

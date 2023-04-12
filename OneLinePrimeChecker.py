
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# Optimized code

is_prime = lambda n: n > 1 and (n == 2 or n % 2 != 0 and all(n % i != 0 for i in range(3, int(n ** 0.5) + 1, 2)))

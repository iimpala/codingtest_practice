import sys

p, n, q = map(int, sys.stdin.readline().strip().split(" "))

# # p^n mod q == (p^(n/2) mod q * p^(n/2) mod q) mod q
# def mod(p, n, q):
#
#     if n == 1:
#         return p % q
#
#     t = mod(p, n // 2, q)
#
#     if n % 2 == 0:
#         return (t * t) % q
#     else:
#         return (p * t * t) % q

# print(mod(p, n, q))

# R to L
r, t = 1, p
while n > 0:
    if n % 2 == 1:
        r = (r * t) % q

    t = (t * t) % q
    n = n // 2

print(r)
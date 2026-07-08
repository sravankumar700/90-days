def primes_up_to(n):
	if n < 2:
		return []
	sieve = bytearray(b"\x01") * (n + 1)
	sieve[0:2] = b"\x00\x00"
	import math
	for p in range(2, int(math.isqrt(n)) + 1):
		if sieve[p]:
			step = p
			start = p * p
			sieve[start:n+1:step] = b"\x00" * (((n - start) // step) + 1)
	return [i for i, is_prime in enumerate(sieve) if is_prime]


def main():
	for p in primes_up_to(10000):
		print(p)


if __name__ == "__main__":
	main()


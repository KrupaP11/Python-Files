###code to run on AI Panter. This code will output the a digit of pi.

import time
import decimal

start_time = time.time()

import decimal

def bbp_pi(n):
    """Calculate the n-th digit of Pi in base 16 (hexadecimal) using the BBP formula."""
    decimal.getcontext().prec = n + 10  # Set precision higher than n to avoid truncation errors
    pi = decimal.Decimal(0)
    
    for k in range(n + 1):
        # BBP formula for Pi in base 16
        pi += (decimal.Decimal(1) / 16**k) * (
            decimal.Decimal(4) / (8 * k + 1) -
            decimal.Decimal(2) / (8 * k + 4) -
            decimal.Decimal(1) / (8 * k + 5) -
            decimal.Decimal(1) / (8 * k + 6)
        )
    
    # Now, extract the n-th digit after the decimal point
    pi_str = str(pi)[2:]  # Remove the "3." part of pi
    return pi_str[n - 1]  # n-th digit (1-indexed)

# Example: Get the nth digit of Pi
n = 10**4
digit = bbp_pi(n)

end_time = time.time()
time_elapsed = end_time - start_time
print("done")

with open("output.txt", "w") as f:
	print(f"The {n}-th digit of Pi in hexadecimal is {digit} and time elapsed is: {time_elapsed}", file=f)


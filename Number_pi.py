###code to run on AI Panter. This code will output the a digit of pi.

import time
from mpmath import mp

start_time = time.time()

mp.dps = 10**4

pi_str = str(mp.pi)

digit = pi_str[mp.dps]

end_time = time.time()

elapsed_time = end_time - start_time

with open("output2.txt", "w") as f:
	print(f"The {mp.dps} digit of pi is: {digit}. \nThe time elapsed is: {elapsed_time}", file=f)

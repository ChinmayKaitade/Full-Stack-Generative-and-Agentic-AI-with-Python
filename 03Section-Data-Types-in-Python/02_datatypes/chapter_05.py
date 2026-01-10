import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.499999999999 # 9.947598300641403e-13
current_temp = 95.49 # 0.010000000000005116
print(f"Ideal temp {ideal_temp}")
print(f"Current temp {current_temp}")
print(f"Difference temp {ideal_temp - current_temp}")

print(sys.float_info) # sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)   
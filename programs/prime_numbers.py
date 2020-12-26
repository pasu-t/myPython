import time
import math

def check_prime_number1(n):
    if n == 1:
        return False
    if n == 2:
        return False
    for i in range(3,int(n/2), 2):
        if n%i == 0:
            return True
    return False

#max devisor for any number is sqrt(number)
def check_prime_number2(n):
    if n == 1:
        return False
    if n == 2 and n%2 == 0:
        return False
    max_divisior = math.floor(math.sqrt(n))
    for i in range(3, max_divisior+1, 2):
        if n%i == 0:
            return True
    return False
start = time.perf_counter()
for num in range(1,100000):
    # print(num, check_prime_number1(num))
    check_prime_number1(num)
stop = time.perf_counter()

print(f"Execution time {stop-start}")

start = time.perf_counter()
for num in range(1,100000):
    # print(num, check_prime_number2(num))
    check_prime_number2(num)
stop = time.perf_counter()

print(f"Execution time {stop-start}")
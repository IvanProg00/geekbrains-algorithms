from datetime import datetime


def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    return fib_calc(n, 0, 1)


def fib_calc(n, prev, cur):
    if n == 0:
        return prev
    elif n == 1:
        return cur

    return fib_calc(n - 1, cur, prev + cur)


n = 30


start_time = datetime.now()
result1 = fib1(n)
print(f"result1: {result1}; speed {datetime.now() - start_time}")


start_time = datetime.now()
result2 = fib2(n)
print(f"result2: {result2}: speed {datetime.now() - start_time}")

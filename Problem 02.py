def fib_iter(k, fib = 1, first = 0, sec = 1):
    while k > 0:
        first, sec, fib = sec, fib, fib+sec
        k -= 1
    return fib

sum_even = 0
num = 0
i = 0
while num <= 4000000:
    if num % 2 == 0:
        sum_even += num
    i += 1
    num = fib_iter(i)

print(sum_even)

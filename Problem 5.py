num = 2520*11*13*17*19
for i in range(20):
    if num % (i+1) != 0:
        num *= ((i+1)/ (num %(i+1)))
print(round(num))

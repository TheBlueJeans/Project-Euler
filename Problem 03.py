num = 600851475143
factors = []
while num > 0:
    exists = False
    for i in range(3, round(num**0.5 + 0.5), 2):
        if num % i == 0:
            factors.append(i)
            num //= i
            exists = True
            break
    if exists == False:
        factors.append(num)
        num = 0
    
highest = 0
for item in factors:
    if item > highest:
        highest = item
print(item)

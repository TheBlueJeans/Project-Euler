triangle = 1
num = 1
combi = 0

while combi <= 500:
    num += 1
    triangle += num
    temp = triangle
    factors = [[1, 1]]

    for i in range(2, 4):
        count = 0
        if temp % i == 0:
            while temp % i == 0:
                count += 1
                temp //= i
        factors.append([i, count])

    while temp > 1:
        for i in range(factors[-1][0], temp+1, 2):
            if temp % i == 0:
                count = 0
                while temp % i== 0:
                    count += 1
                    temp //= i
                factors.append([i, count])
                break

    combi = 1
    for i in range(1, len(factors)):
        combi *= (factors[i][1]+1)

print(triangle)

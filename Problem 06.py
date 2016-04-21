total_sum = 0
total_sq = 0
for i in range(1, 101):
    total_sum += i**2
    total_sq += i
diff = total_sq**2 - total_sum
print(diff)

found = False
for i in range(999**2, 100**2, -1):
    string = str(i)
    if string == string[::-1]:
        for j in range(101, round(i**0.5 + 0.5)):
            if i % j == 0 and len(str(i//j)) == 3:
                found = True
                break
        if found == True:
            break
print(i)

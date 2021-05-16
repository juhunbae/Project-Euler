x = 600851475143
y = []
for i in range(2, x / 2):
    if (x % i) == 0:
        y.append(i)
print(y[-1])
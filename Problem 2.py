x = [1, 2]
y = []
while x[-1] + x[-2] <= 4000000:
    a = x[-1] + x[-2]
    x.append(a)
for i in range(len(x)):
    if x[i] % 2 == 0:
        y.append(x[i])
print(sum(y))
n = 30 # število ljudi v sobi
p = 1
for i in range(1, n):
    p = p * (1 - (i/365))

print(1 - p)
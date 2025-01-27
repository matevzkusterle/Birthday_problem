n = 30 # Number of people in the room. You can change this parameter.
p = 1
for i in range(1, n):
    p = p * (1 - (i/365))

print(1 - p)
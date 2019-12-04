import math

mone = int(input())
denominations = [1, 3, 4]
mincoins = [0] + [math.inf]*mone

for i in range(1, mone+1):
    for j in denominations:
        if i>=j:
            coins = mincoins[i-j]+1
            if coins < mincoins[i]:
                mincoins[i] = coins

print(mincoins[mone])
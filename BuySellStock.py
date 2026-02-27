# runtime:28ms

prices = [10,1,5,6,7,1]

maxP = 0
suffix = [0]*len(prices)
maxProfit = 0

for i in range(len(prices)-1,-1,-1):
    maxP = max(maxP,prices[i])
    suffix[i] = maxP

for i in range(len(prices)):
    sell = suffix[i] - prices[i]
    maxProfit = max(sell,maxProfit)

print(maxProfit)


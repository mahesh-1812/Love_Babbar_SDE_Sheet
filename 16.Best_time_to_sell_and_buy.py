#16.Best time to sell and buy

#approach 1
def sellandbuy(prices):
    buy_1=min(prices)
    for i in range(len(prices)):
        if prices[i]<=buy_1:
            buy_1=prices[i]
        if prices[-1]==(1 or 0):
            return 0
    sell_1=max(prices)
    profit=sell_1-buy_1
    for j in range(len(prices)):
        if prices[j]==profit:
            return j+1

#Approach 2
def sellandbuy1(prices):
    l=0
    r=1
    max_profit=0
    while r<len(prices):
        cur_proft=prices[r]-prices[l]
        if prices[l]<prices[r]:
            max_profit=max(max_profit,cur_proft)
        else:
            l=r
            r+=1
    return max_profit
  
sellandbuy(prices=[7,6,4,3,1])

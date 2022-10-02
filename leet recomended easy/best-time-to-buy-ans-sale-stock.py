class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        bought = prices[0]
        
        for price in prices:
            if price > bought:
                sum += price-bought
            bought = price
        
        return sum
"""
Idea: only the following item metters, as you can buy and sale as many times as yu like, but cant hold more then 1 stock at a time

What did i learn? nothing i can put my finger on
  


"""

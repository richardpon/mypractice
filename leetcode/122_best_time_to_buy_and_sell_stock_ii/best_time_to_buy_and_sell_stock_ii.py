from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        #maybe buy on day n
        #if next day cheaper, then reset and maybe buy that day
        
        #if next day is higher, maybe sell
        #if next day lower, sell day before
        #if next day higher (or last day), maybe sell, but don't

        total_profit = 0

        #maybe buy or sell
        buy_price = prices[0]
        sell_price = None

        for price in prices[1:]:
            
            if sell_price is None:
                # do I have a potential sell price, or better buy?
                if price > buy_price:
                    # have potential sale (price went up)
                    sell_price = price
                else:
                    # buy this day instead
                    buy_price = price
            else:
                # have a potential sale price
                if price >= sell_price:
                    # price went up, sell this day instead
                    sell_price = price
                else:
                    #price went down, should sell yesterday(buy today)
                    cur_profit = sell_price - buy_price
                    total_profit += cur_profit

                    #buy today (sold yesterday, buy today)
                    buy_price = price
                    sell_price = None

        #should sell when done?
        if sell_price and sell_price > buy_price:
            cur_profit = sell_price - buy_price
            total_profit += cur_profit

        return total_profit

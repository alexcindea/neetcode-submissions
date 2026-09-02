class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = math.inf
        #minimum value before each i position
        local_min = prices[0]
        #best profit we can find
        max_prof = 0
        for i in range(len(prices)):
            #consider the value for the current position, use the minimum up until that point to determine the profit
            if prices[i] < local_min:
                local_min = prices[i]
            current_profit = prices[i] - local_min
            print(f"at index: {i}, price[i]: {prices[i]}")
            print(f"current profit: {current_profit}")
            print(f"local_min: {local_min}")

            max_prof = current_profit if max_prof < current_profit else max_prof
            print(f"max_profit is: {max_prof}")

        return max_prof


        
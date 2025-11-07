"""
LeetCode 121: Best Time to Buy and Sell Stock

Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Approach:
        - Keep track of the minimum price seen so far
        - For each day, calculate profit if we sell on that day
        - Update max profit if current profit is greater
        """
        if not prices or len(prices) < 2:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            # Update minimum price seen so far
            min_price = min(min_price, prices[i])
            
            # Calculate profit if we sell on day i
            profit = prices[i] - min_price
            
            # Update maximum profit
            max_profit = max(max_profit, profit)
        
        return max_profit


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Input: {prices1}")
    print(f"Output: {solution.maxProfit(prices1)}")  # Expected: 5
    print()
    
    # Example 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Input: {prices2}")
    print(f"Output: {solution.maxProfit(prices2)}")  # Expected: 0
    print()
    
    # Additional test case
    prices3 = [10, 1, 5, 4, 7, 1]
    print(f"Input: {prices3}")
    print(f"Output: {solution.maxProfit(prices3)}")  # Expected: 6


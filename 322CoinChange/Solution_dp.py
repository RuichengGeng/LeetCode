# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 11:07:50 2021

@author: Ruich
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse = True) # order coins from big to small
        dp = [0] + [float("inf")] *amount
        
        for coin in coins:
            for i in range(coin,amount + 1):
                dp[i] = min(dp[i],dp[i - coin] + 1)
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]
        
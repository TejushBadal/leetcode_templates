# Coin Change (LC 322)
# BLIND 75 ✅ | Medium | Optimization DP - Unbounded Knapsack
# TIME: Day 7: 8 min (with heavy guidance - need Day 11 independent review)
# MARKED FOR: Day 11 review (solve from scratch, derive recurrence)
# 
# ═══════════════════════════════════════════════════════════════
# PROBLEM TYPE: Unbounded Knapsack / Optimization DP
# ═══════════════════════════════════════════════════════════════
# Given: coins[] (unlimited quantity), amount
# Question: Minimum coins to make amount? (-1 if impossible)
#
# ═══════════════════════════════════════════════════════════════
# KEY INSIGHT: For each amount, try ALL coins!
# ═══════════════════════════════════════════════════════════════
# To make amount i:
#   - Try coin c → need 1 coin + dp[i-c]
#   - Try ALL coins, take MIN
#
# Recurrence: dp[i] = min(dp[i-coin] + 1) for all coins <= i
#
# ═══════════════════════════════════════════════════════════════
# CRITICAL: Initialization with Infinity!
# ═══════════════════════════════════════════════════════════════
# dp[i] = inf means "can't make amount i (yet)"
# If dp[amount] == inf after trying all → impossible, return -1
#
# ═══════════════════════════════════════════════════════════════
# COMPLEXITY:
# ═══════════════════════════════════════════════════════════════
# Time: O(amount × len(coins)) - for each amount, try all coins
# Space: O(amount) - DP array
#
# ═══════════════════════════════════════════════════════════════
# CODE:
# ═══════════════════════════════════════════════════════════════
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# ═══════════════════════════════════════════════════════════════
# PATTERN PROGRESSION:
# ═══════════════════════════════════════════════════════════════
# Climbing Stairs: SUM (dp[i] = dp[i-1] + dp[i-2])
# House Robber: MAX + decision (dp[i] = max(...))
# Coin Change: MIN + unbounded (try all, take min)
#
# ═══════════════════════════════════════════════════════════════
# VARIATIONS:
# ═══════════════════════════════════════════════════════════════
# - Coin Change II (LC 518): Count WAYS (not min coins)
# - Perfect Squares (LC 279): Same pattern, coins = [1,4,9,16,...]
# - Min Cost Climbing Stairs (LC 746): Similar optimization DP
#
# ═══════════════════════════════════════════════════════════════
# MY NOTES:
# ═══════════════════════════════════════════════════════════════
# MY CONFUSION: Deriving recurrence independently (needed guidance)
# MY LEARNING: Infinity initialization for "impossible/unknown"
#              Unbounded = can use each coin unlimited times
# DIFFICULTY FELT: 8/10 (concept hard, needed template + recurrence)
# Climbing Stairs (LC 70)
# BLIND 75 ✅ | Easy | DP Foundation - Fibonacci Pattern
# TIME: Day 7: 5 min (**MASTERED** - This is your DP baseline!)
# 
# ═══════════════════════════════════════════════════════════════
# KEY INSIGHT: THIS IS THE DP FOUNDATION!
# ═══════════════════════════════════════════════════════════════
# To reach step n, you came from either:
#   - Step n-1 (climb 1 step) OR
#   - Step n-2 (climb 2 steps)
# 
# Recurrence: dp[i] = dp[i-1] + dp[i-2]
# This is FIBONACCI!
#
# ═══════════════════════════════════════════════════════════════
# COMPLEXITY:
# ═══════════════════════════════════════════════════════════════
# Time: O(n) - fill n entries
# Space: O(n) - dp array (can optimize to O(1) with 2 variables)
#
# ═══════════════════════════════════════════════════════════════
# CODE:
# ═══════════════════════════════════════════════════════════════
def climbStairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# ═══════════════════════════════════════════════════════════════
# O(1) SPACE OPTIMIZATION (Optional):
# ═══════════════════════════════════════════════════════════════
# Only keep last 2 values (prev2, prev1)
# Space: O(n) → O(1)
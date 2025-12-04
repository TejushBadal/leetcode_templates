# ## Jump Game (LC 55) - MEDIUM - Blind 75 ✅
# **Date Solved:** Nov 5, 2024 (Day 9)
# **Time Taken:** ~20 min (15 min exploration + 5 min correct implementation)
# **Pattern:** Greedy - Track Furthest Reachable

# ### Problem:
# Given array where nums[i] = max jump length from position i.
# Starting at index 0, can you reach the last index?

# ### Key Insight - Greedy, Not DP!
# **Wrong approach (my first try):** Jump to position with max value  
# **Correct approach:** Track furthest position reachable

# **Why greedy works:**
# - If we can reach position i, we can reach ANY position ≤ i
# - Don't need to try all paths - just track maximum reach
# - If max reach ≥ last index → guaranteed success!

# Pattern Recognition - When Greedy Works:
# ✅ Track "furthest/best so far"
# ✅ Local decision doesn't affect future options
# ✅ Can prove local optimal leads to global optimal
# ✅ Examples: Jump Game, Gas Station, Best Time to Buy/Sell Stock

# ### Approach:
# 1. Track `furthest` position reachable (starts at 0)
# 2. For each position i:
#    - If i > furthest → stuck, return False
#    - Update furthest = max(furthest, i + nums[i])
#    - If furthest ≥ last index → return True
# 3. If loop completes → return False

# ### Time Complexity: O(n)
# - Single pass through array
# - Each position: O(1) work

# ### Space Complexity: O(1)
# - Only track one variable (furthest)

# ### Complete Solution (Forward Pass):
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        
        for i in range(len(nums)):
            # Stuck: current position beyond reach
            if i > furthest:
                return False
            
            # Update furthest reachable
            furthest = max(furthest, i + nums[i])
            
            # Can reach end!
            if furthest >= len(nums) - 1:
                return True
        
        return False
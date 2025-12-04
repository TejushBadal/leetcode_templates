## HOUSE ROBBER 
## 1D DP -- DECISION PATTERN
###O(n) time, O(n) space?


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0]*n
        #edge cases
        if n ==1:
            return nums[0]
        if n ==2:
            return max(nums[0], nums[1])

        #base cases 0 and 1
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1]) #since we want to start with max

        for i in range(2,n):
            #current = max of decision (rob or skip)
            print(i)
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[n-1]

# ## House Robber II (LC 213) - MEDIUM - Blind 75 ✅
# **Date Solved:** Nov 5, 2024 (Day 9)
# **Time Taken:** 10 min (adapted House Robber I pattern!)
# **Pattern:** Dynamic Programming - Circular Constraint (2-Pass DP)

# ### Problem:
# Houses arranged in a circle. Rob houses to maximize money, but:
# - Cannot rob two adjacent houses
# - **First and last houses are NEIGHBORS (circular)**

# ### Key Insight - Circular Constraint:


# **Cannot solve circular constraint with single DP pass!**

# ### Approach - Break the Circle:
# 1. **Case 1:** Rob house 0 → exclude last house → solve [0 to n-2]
# 2. **Case 2:** Don't rob house 0 → can rob last → solve [1 to n-1]
# 3. Return max of both cases

# **This reduces to 2× House Robber I (linear)!**

# ### Time Complexity: O(n)
# - Run House Robber helper twice: 2 × O(n) = O(n)
# - Each pass: iterate through n houses once

# ### Space Complexity: O(n)
# - DP array in helper function: O(n)
# - Two calls don't stack (sequential, not nested)

### Complete Solution:
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: only 1-2 houses (no real circular constraint)
        if len(nums) <= 2:
            return max(nums)
        
        # Helper: House Robber I (linear)
        def rob_linear(houses):
            n = len(houses)
            dp = [0] * n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            
            for i in range(2, n):
                dp[i] = max(houses[i] + dp[i-2], dp[i-1])
            
            return dp[-1]  # Or max(dp) - same result
        
        n = len(nums)
        
        # Case 1: Rob first, exclude last [0 to n-2]
        rob_first = rob_linear(nums[0:n-1])
        
        # Case 2: Exclude first, can rob last [1 to n-1]
        skip_first = rob_linear(nums[1:n])
        
        return max(rob_first, skip_first)


# ## Decode Ways (LC 91) - MEDIUM - Blind 75 ✅
# **Date Solved:** Nov 5, 2024 (Day 9)
# **Time Taken:** ~25 min (with guidance on recurrence + zero handling)
# **Pattern:** Dynamic Programming - Decision DP with Constraints (Fibonacci-like)

# ### Problem:
# Decode a string of digits where 'A'=1, 'B'=2, ..., 'Z'=26.
# Return number of ways to decode the string.
# - Can decode 1 or 2 digits at a time
# - '0' cannot be decoded standalone (only as second digit in 10-20)

# ### Key Insight - Similar to Climbing Stairs:

# Climbing Stairs: dp[i] = dp[i-1] + dp[i-2]
# (1 step OR 2 steps)

# Decode Ways: dp[i] = dp[i-1] (if single valid) + dp[i-2] (if double valid)
# (1 digit OR 2 digits)


# **BUT with constraints:** Only add if decode is valid!

# ### Approach:
# 1. **State:** dp[i] = number of ways to decode first i characters
# 2. **Base cases:**
#    - dp[0] = 1 (empty string: 1 way)
#    - dp[1] = 1 (first char, if not '0')
# 3. **Transitions (two decisions):**
#    - **Single digit:** If s[i-1] is '1'-'9' → dp[i] += dp[i-1]
#    - **Two digits:** If s[i-2:i] is 10-26 → dp[i] += dp[i-2]
# 4. **Edge case:** If string starts with '0' or is empty → return 0

# ### Time Complexity: O(n)
# - Single pass through string: O(n)
# - Each position: O(1) work (check single/double digit)

# ### Space Complexity: O(n)
# - DP array of size n+1: O(n)
# - Can optimize to O(1) with two variables (like Fibonacci)

# ### Complete Solution:
class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: empty or starts with '0'
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # Empty string: 1 way
        dp[1] = 1  # First character (already checked not '0')
        
        # Fill DP with decisions
        for i in range(2, n + 1):
            # Decision 1: Decode single digit (if 1-9)
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Decision 2: Decode two digits (if 10-26)
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]
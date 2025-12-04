# ## Subsets (LC 78) - MEDIUM - Blind 75 ✅
# **Date Solved:** Nov 5, 2024 (Day 9)
# **Time Taken:** 6 min ⚡ (cleanest backtracking yet!)
# **Pattern:** Backtracking - Power Set (Include/Exclude Each Element)

# ### Problem:
# Given integer array `nums` of unique elements, return all possible subsets (the power set).
# - Order doesn't matter: [1,2] = [2,1] (same subset)
# - Include empty set
# - 2^n total subsets

# ### Approach:
# 1. Add current subset to result at EVERY recursive call (not just at end!)
# 2. For each element from start_index onwards: decide to include or exclude
# 3. Include: add to current, recurse with i+1, backtrack (pop)
# 4. Exclude: just move to next element (handled by loop)
# 5. Use start_index to prevent duplicates ([1,2] and [2,1])

# ### Key Insight - Decision Tree:
# nums = [1,2,3]

#             []
#            /  \
#      (inc 1) (skip 1)
#         /  \      /  \
#   (inc 2)(skip)(inc 2)(skip)
#     /\    /\     /\     /\
#  [123][12][13][1][23][2][3][]
# Each level: Include current element OR skip it
# Result: 2^n subsets (2 choices per element)

### Time Complexity: O(2^n × n)
# - Total subsets: 2^n (each element: include or exclude)
# - Copy each subset to result: O(n)
# - **Total: O(2^n × n)**

# **Why 2^n?**
# - n=1: [[], [1]] = 2 subsets
# - n=2: [[], [1], [2], [1,2]] = 4 subsets
# - n=3: 8 subsets
# - Pattern: 2^n

# ### Space Complexity: O(n)
# - Recursion depth: O(n) - at most n elements deep
# - Current subset: O(n)
# - **Total: O(n)** (not counting output storage of 2^n subsets)

### Complete Solution:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start_index, current):
            # Add current subset (ALWAYS valid!)
            result.append(current.copy())  # MUST COPY!
            
            # Try including each remaining element
            for i in range(start_index, len(nums)):
                # Include nums[i]
                current.append(nums[i])
                
                # Recurse with i+1 (move forward, no reuse)
                backtrack(i + 1, current)
                
                # Backtrack (exclude nums[i])
                current.pop()
        
        backtrack(0, [])
        return result
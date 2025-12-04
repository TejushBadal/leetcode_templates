# ## Permutations (LC 46) - MEDIUM - Blind 75 ✅
# **Date Solved:** Nov 4, 2024 (Day 8)
# **Time Taken:** ~20 min (followed template after analysis)
# **Pattern:** Backtracking - All Orderings (Order Matters!)

# ### Problem:
# Given array of distinct integers, return all possible permutations.
# - Order matters: [1,2] ≠ [2,1]
# - Each element used exactly once per permutation

# ### Approach:
# 1. Try ALL elements at each step (not just from index onwards)
# 2. Track used elements in current permutation with set
# 3. When permutation length == input length → complete!
# 4. Backtrack: Remove from both current list AND used set

# ### Time Complexity: O(n! × n)
# - Number of permutations: n! (factorial)
# - Build each permutation: O(n) to copy to result
# - **Total: O(n! × n)**

# **Why n! is massive:**
# - n=3: 6 permutations
# - n=5: 120 permutations  
# - n=10: 3,628,800 permutations (over 3 million!)

# ### Space Complexity: O(n)
# - Recursion depth: O(n) - build one element at a time
# - Used set: O(n) - track at most n elements
# - Current permutation: O(n)
# - **Total: O(n)** (not counting output)

### Complete Solution:

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = set()
        
        def backtrack(current):
            # Base case: complete permutation
            if len(current) == len(nums):
                result.append(current.copy())  # MUST COPY!
                return
            
            # Try every element (order matters!)
            for num in nums:
                if num not in used:
                    # Make choice
                    used.add(num)
                    current.append(num)
                    
                    # Recurse (no index needed!)
                    backtrack(current)
                    
                    # Undo choice (TWO steps!)
                    current.pop()
                    used.remove(num)
        
        backtrack([])
        return result
# ## Combination Sum (LC 39) - MEDIUM - Blind 75 ✅
# **Date Solved:** Nov 4, 2024 (Day 8)
# **Time Taken:** 16 min (6 min coding after template guidance)
# **Pattern:** Backtracking - Reusable Elements (Unbounded)

# ### Problem:
# Find all unique combinations in candidates where numbers sum to target.
# - Same number can be used UNLIMITED times
# - Combinations must be unique

# ### Approach:
# 1. Backtracking with index tracking (prevents duplicates)
# 2. Pass `start_index` to recurse - only explore from current index onwards
# 3. Can REUSE same element: pass `i` not `i+1` to recursion
# 4. Prune when sum > target (optimization)
# 5. Add to result when sum == target

# ### Time Complexity: O(n^(target/min))
# **Exponential!** Decision tree analysis:
# - At each level: n choices (pick any candidate)
# - Tree depth: target / min_candidate
# - Total nodes: n × n × n × ... (target/min times)
# - Example: candidates=[1], target=100 → depth 100, branches n each level

# **Why LeetCode says "< 150 solutions":** Constraints chosen to keep it manageable.

# ### Space Complexity: O(target/min)
# - Recursion stack depth: target / min_candidate (how deep we go)
# - Current combination storage: O(target/min) worst case
### Complete Solution:
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start_index, current_combination, current_sum):
            # Base case: found valid combination
            if current_sum == target:
                result.append(current_combination.copy())  # MUST COPY!
                return
            
            # Base case: exceeded target (prune)
            if current_sum > target:
                return
            
            # Try each candidate from start_index onwards
            for i in range(start_index, len(candidates)):
                # Make choice
                current_combination.append(candidates[i])
                
                # Recurse: pass i (not i+1) - can REUSE same element!
                backtrack(i, current_combination, current_sum + candidates[i])
                
                # Undo choice (BACKTRACK!)
                current_combination.pop()
        
        backtrack(0, [], 0)
        return result
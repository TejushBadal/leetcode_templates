# ## Longest Consecutive Sequence (LC 128) - MEDIUM - Blind 75 ✅
# **Date Solved:** Nov 6, 2024 (Day 10)
# **Time Taken:** 11 min (9 min + 2 min bug fix)
# **Pattern:** Hash Set - Sequence Detection (Optimal O(n) without sorting!)

# ### Problem:
# Given unsorted array of integers, find length of longest consecutive sequence.
# - Must run in O(n) time (can't sort!)

# ### Key Insight - Only Start from Sequence Beginnings:
# **Naive:** Count forward from EVERY number → O(n²)  
# **Optimal:** Only count from START of sequences → O(n)

# **How to detect start?** If `num - 1` not in set → it's a start!

# ### Approach:
# 1. Put all numbers in hash set (O(1) lookup)
# 2. For each unique number:
#    - Check if `num - 1` exists → if YES, skip (not a start)
#    - If NO → count consecutive: num, num+1, num+2, ...
# 3. Track max length

# ### Time Complexity: O(n)
# **Why not O(n²) with nested loop?**
# - Each number visited at most TWICE:
#   1. Once to check if it's a start
#   2. Once when counting from actual start
# - Amortized: Each number counted exactly once as part of sequence

# ### Space Complexity: O(n)
# - Hash set stores all unique numbers

# ### Complete Solution:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique_nums = set(nums)
        longest_sequence = 0

        for num in unique_nums:  # MUST iterate over set, not array!
            if (num - 1) not in unique_nums:  # Sequence start
                current_num = num
                current_sequence = 1
                
                while (current_num + 1) in unique_nums:
                    current_num += 1
                    current_sequence += 1
                
                longest_sequence = max(current_sequence, longest_sequence)
        
        return longest_sequence
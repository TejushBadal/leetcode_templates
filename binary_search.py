# PATTERN: Binary Search - Find Minimum in Rotated Sorted Array
# PROBLEM: LC 153

# TEMPLATE:
# MY MISTAKE:
# - Initially tried nested if statements checking nums[low] < nums[high]
# - Overcomplicated the logic - only needed ONE comparison
# - Used mid+1 and mid-1 incorrectly, didn't understand when to include mid

# MY KEY INSIGHT:
# - nums[mid] > nums[high] means minimum is DEFINITELY right of mid (mid can't be answer)
# - nums[mid] <= nums[high] means minimum is mid OR left of mid (keep mid with high=mid)

# TIME: 35 min (25 min initial + 10 min fix)
# DIFFICULTY: Medium but felt easy after yesterday's rotated search problem
def find_min_rotated(nums):
    low, high = 0, len(nums) - 1
    
    while low < high:  # Converge to single element
        mid = low + (high - low) // 2
        
        # Compare mid with right boundary
        if nums[mid] > nums[high]:
            # Rotation point is in right half
            # Minimum must be to the right of mid
            low = mid + 1
        else:
            # Right half is sorted
            # Minimum is at mid or to the left
            high = mid  # Keep mid as potential answer
    
    return nums[low]  # low == high at this point

# COMPLEXITY: O(log n) time, O(1) space

# KEY INSIGHTS:
# - Compare nums[mid] with nums[high] (not nums[low])
# - If nums[mid] > nums[high]: array "breaks" in right half
# - Use "high = mid" (not mid-1) because mid could be the answer
# - while low < high (not <=) because we want them to converge

# COMPARISON TO "SEARCH IN ROTATED SORTED ARRAY":
# - That problem: Find target (needs more conditions)
# - This problem: Find minimum (simpler - just one comparison)
# - Both use same rotation detection logic

# EDGE CASES:
# - No rotation: [1,2,3,4,5] → returns 1
# - Full rotation: [2,3,4,5,1] → returns 1
# - Two elements: [2,1] → returns 1
# - Single element: [1] → returns 1

# SIMILAR PROBLEMS:
# - LC 154: Find Minimum in Rotated Sorted Array II (with duplicates)
# - LC 33: Search in Rotated Sorted Array (yesterday's problem)
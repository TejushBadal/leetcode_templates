from collections import Counter, defaultdict

def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""
    
    target = Counter(t)
    window = defaultdict(int)
    
    # WHY len(target) not len(t)? _______________
    required = len(target)
    
    # WHAT does formed track exactly? _______________
    formed = 0
    
    left = 0
    result = float("inf"), None, None
    
    for right in range(len(s)):
        letter = s[right]
        window[letter] += 1
        
        # WHY check == target[letter]? _______________
        if letter in target and window[letter] == target[letter]:
            formed += 1
        
        # Shrink when valid
        while required == formed:
            # Update result
            if result[0] > right - left + 1:
                result = right - left + 1, left, right
            
            left_letter = s[left]
            
            # WHY this specific condition? _______________
            # WHY not just "if left_letter in target"? _______________
            if left_letter in target and window[left_letter] == target[left_letter]:
                formed -= 1
            
            # WHY decrement AFTER checking formed? _______________
            window[left_letter] -= 1
            left += 1
    
    return s[result[1]:result[2]+1] if result[1] is not None else ""

# MY KEY INSIGHT: formed tracks the NUMBER OF UNIQUE CHARACTERS 
# that have reached their required count, NOT total character count
# 
# Decrement formed only at the TRANSITION point (== check BEFORE decrement)
# because that's when a character goes from satisfied → unsatisfied
#
# TIME: Day 3: 70min, Day 5: 40min
# COMPLEXITY: Time O(n), Space O(|S|+|T|) where S,T = unique chars
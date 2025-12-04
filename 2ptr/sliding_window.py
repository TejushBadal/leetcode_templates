#PATTERN --> Sliding window + HASH MAP
#PROBLEM --> Minimum Window Substring (HARD)
#COMPLEXITY --> N time, k space

#WHEN TO USE --> finding substring/subarray WITH CONSTRAINTS
#SIMILAR PROBS --> longest sub without repeating chars, permutation in string

#TEMPLATE
from collections import Counter, defaultdict
def sliding_window(s, t):

    needed_chars = Counter(t)
    window = defaultdict(int)
    left = 0
    num_valid = 0

    result = tuple()
    #now sliding window, expand right invalid, shrink left valid

    for right in range(len(s)):

        letter = s[right]
        window[letter] +=1
        #expand
        if letter in needed_chars and window[letter] == needed_chars[letter]:
            num_valid +=1

        #shrink if valid

        while num_valid == len(needed_chars):
            #if this current one is smaller/larger/wtv q asks
            #update result 
            cur_letter = s[left]

            if cur_letter in needed_chars and window[cur_letter] == needed_chars[cur_letter]:
                num_valid -=1
            window[cur_letter] -=1

            left +=1
    
    return result



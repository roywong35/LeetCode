def lengthOfLongestSubstring(s: str) -> int:
    if len(s) < 2:
        return len(s)
    
    seen = {}
    longest = 0
    left = 0
    
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        length = right - left + 1
        longest = max(longest, length)
        
    return longest
print(lengthOfLongestSubstring(s = ""))
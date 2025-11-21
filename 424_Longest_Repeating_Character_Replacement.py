from collections import defaultdict

def characterReplacement(s: str, k: int) -> int:
    count = defaultdict(int)
    max_count = 0
    left = 0
    longest = 0
    
    for right, char in enumerate(s):
        count[char] += 1
        max_count = max(max_count, count[char])
        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
            
        longest = max(longest, right - left + 1)
        
    return longest

print(characterReplacement(s = "AABABBA", k = 1))
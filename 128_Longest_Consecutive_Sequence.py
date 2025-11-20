def longestConsecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0

    for x in nums:
        if x - 1 not in num_set:
            length = 1
            while x + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest

print(longestConsecutive([100,4,200,1,3,2]))
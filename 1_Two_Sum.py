def twoSum(nums, target):
    seen = {}
    
    for i, val in enumerate(nums):
        complment = target - val
        if complment not in seen:
            seen[val] = i
        else:
            return [seen[complment], i]

print(twoSum(nums = [3,3], target = 6))
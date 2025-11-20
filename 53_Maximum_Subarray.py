def maxSubArray(nums: list[int]) -> int:
    curr_sum = nums[0]
    max_sum = 0
    
    for x in nums:
        curr_sum = max(curr_sum + x, x)
        max_sum = max(max_sum, curr_sum)
        
    return max_sum
print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))

def maxSubArray(nums: list[int]) -> int:
    res = nums[0]
    total = 0
    
    for x in nums:
        if total < 0:
            total = 0
    
        total += x
        res = max(res, total)
            
    return res
print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
def productExceptSelf(nums: list[int]) -> list[int]:
    left = right = 1
    res = [1] * len(nums)
    
    for i in range(len(nums)):
        res[i] *= left
        left *= nums[i]
        
    for i in range(len(nums)-1, -1, -1):
        res[i] *= right
        right *= nums[i]
     
    return res

print(productExceptSelf(nums = [1,2,3,4]))
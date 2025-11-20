def maxProduct(nums: list[int]) -> int:
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        n = nums[i]
        
        if n < 0:
            max_prod, min_prod = min_prod, max_prod
            
        max_prod = max(n, n * max_prod)
        min_prod = min(n, n * min_prod)
        
        result = max(result, max_prod)
        
    return result


print(maxProduct(nums = [2,-5,-2,-4,3]))
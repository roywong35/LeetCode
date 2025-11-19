def nextGreaterElements(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(2*n-1, -1 , -1):
        num = nums[i % n]
        while stack and num >= nums[stack[-1]]:
            stack.pop()

        if i < n:
            if stack:
                res[i] = nums[stack[-1]]
        
        stack.append(i % n)

    return res

print(nextGreaterElements(nums = [1,2,3,4,3]))
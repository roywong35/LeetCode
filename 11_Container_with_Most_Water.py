def maxArea(height: list[int]) -> int:
    max_area = curr = 0
    left = 0
    right = len(height) - 1

    while left < right:
        h = min(height[left], height[right])
        curr = h * (right - left)
        max_area = max(max_area, curr)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

print(maxArea(height = [1,1]))
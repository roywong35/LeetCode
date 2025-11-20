def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

print(containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))
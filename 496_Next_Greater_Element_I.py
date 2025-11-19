def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    record = {}
    stack = []

    for i in range(len(nums2) - 1, -1, -1):
        while stack and stack[-1] <= nums2[i]:
            stack.pop()

        if not stack:
            record[nums2[i]] = -1
        else:
            record[nums2[i]] = stack[-1]

        stack.append(nums2[i])

    return [record[x] for x in nums1]

print(nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
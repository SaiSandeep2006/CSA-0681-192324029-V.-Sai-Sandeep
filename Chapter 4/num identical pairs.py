def numIdenticalPairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count

# Example 1
nums1 = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums1))  # Output: 4

# Example 2
nums2 = [1, 1, 1, 1]
print(numIdenticalPairs(nums2))  # Output: 6

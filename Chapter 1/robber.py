def rob(nums):
    def rob1(h):
        p1 = p2 = 0
        for num in nums:
             p1, p2 = max(num + p2, p1), p1
        return p1
    if len(nums) == 1:
        return nums[0]    
    return max(rob(nums[:-1]), rob(nums[1:]))
print(rob([1,2,3,1]))  
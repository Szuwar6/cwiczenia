def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1;
                r -= 1
    return res


print(threeSum([1, 1, 3, 4, -2, -4]))



def mySqrt(x) -> int:
    r = x
    while r*r > x:
        r = (r + x/r) / 2
    return int(r)

print(mySqrt(144))



def missingNumber(nums):
        nums.sort()

        if nums[0] == 0 and len(nums) == 1:
            return 1
        if nums[0] == 1 and len(nums) == 1:
            return 0
        if nums[0] != 0:
            return 0
        if nums[-1] == len(nums) - 1:
            return nums[-1] + 1

        for i in range(len(nums)):

            if nums[i + 1] - nums[i] == 1:
                i += 1
            else:
                return nums[i + 1] - 1

print(missingNumber([0 , 1  , 2,3 , 4 ,6]))



def maxSubArray(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


class Worker:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Worker(fname='{self.fname}', lname='{self.lname}')"


worker = Worker('Mike', 'Smith')
print(worker)
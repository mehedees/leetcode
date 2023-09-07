class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = len(nums)
        n = k
        nums.sort()
        if k == 0 or val < nums[0] or val > nums[-1]:
            return k
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
                k -= 1
            if i + 1 < n and nums[i + 1] > val:
                break
        nums.sort(reverse=True)
        return k


if __name__ == '__main__':
    s = Solution()
    nums = [3,2,2,3]
    val = 2
    r = s.removeElement(nums, val)
    print(r, nums[:r])

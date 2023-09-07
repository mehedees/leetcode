class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = list(x for x in nums if x != val)
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [3,2,2,3]
    val = 2
    r = s.removeElement(nums, val)
    print(r, nums[:r])


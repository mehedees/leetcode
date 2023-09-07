class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2]
    r = s.removeDuplicates(nums)
    print(r, nums[:r])

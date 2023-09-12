class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        hmap = dict()
        index = 0
        for i in range(len(nums)):
            k = hmap.get(nums[i], 0)
            if k == 0:
                hmap[nums[i]] = 1
                nums[index] = nums[i]
                index += 1
            elif k == 1:
                hmap[nums[i]] = 2
                nums[index] = nums[i]
                index += 1

        return index


if __name__ == '__main__':
    s = Solution()
    nums = []
    r = s.removeDuplicates(nums)
    print(r, nums[:r])

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        elif n > 0:
            if nums2[0] >= nums1[m-1]:
                for i in range(n):
                    nums1[m+i] = nums2[i]
            elif nums1[0] >= nums2[-1]:
                for i in range(m):
                    nums1.pop()
                    nums1.insert(i, nums2[i])
            else:
                mi: int = 0
                ni: int = 0
                for _ in range(len(nums1)):
                    print(nums1, mi, ni)
                    if mi >= (m+n) or ni >= n:
                        break
                    else:
                        if nums1[mi] == nums2[ni]:
                            nums1.insert(mi, nums2[ni])
                            nums1.pop()
                            mi += 1
                            ni += 1
                        elif nums1[mi] > nums2[ni]:
                            nums1.insert(mi, nums2[ni])
                            nums1.pop()
                            mi += 1
                            ni += 1
                        elif nums1[mi] < nums2[ni]:
                            if mi < m+ni:
                                mi += 1
                            else:
                                nums1[mi:] = nums2[ni:]
                                break

        print(nums1)


if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1, m, nums2, n)


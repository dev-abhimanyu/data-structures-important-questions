# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        res = []
        for i in range(min(k, len(nums1))):
            heappush(heap, ((nums1[i] + nums2[0]), i, 0))
        counter = 1
        while heap and counter <= k:
            sum_value, u, v = heappop(heap)
            res.append((nums1[u],nums2[v]))
            v += 1
            if v < len(nums2):
                heappush(heap, ((nums1[u]+nums2[v]), u, v))
            counter += 1
        return res
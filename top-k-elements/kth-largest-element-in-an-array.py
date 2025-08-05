# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(0, k):
            heappush(heap, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heappop(heap)
                heappush(heap, nums[i])
        return heap[0]
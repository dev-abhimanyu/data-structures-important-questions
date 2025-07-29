# https://leetcode.com/problems/kth-largest-element-in-a-stream/
from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.heap = self.nums[:k]
        heapify(self.heap)
        for element in self.nums[k:]:
            if element > self.heap[0]:
                heappop(self.heap)
                heappush(self.heap, element)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
            if len(self.heap) == self.k:
                return self.heap[0]
        else:    
            if val > self.heap[0]:
                heappop(self.heap)
                heappush(self.heap, val)
            return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
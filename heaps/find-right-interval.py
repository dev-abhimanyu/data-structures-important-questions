# https://leetcode.com/problems/find-right-interval/
import heapq
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_heap = []
        end_heap = []
        n = len(intervals)
        result = [-1] * n
        # populate the heaps
        for i in range(n):
            heapq.heappush(start_heap, (intervals[i][0], i))
            heapq.heappush(end_heap, (intervals[i][1], i))
        while end_heap:
            end, index = heapq.heappop(end_heap)
            # Remove all start points from start_heap that are smaller than the current end point.
            while start_heap and start_heap[0][0] < end:
                heapq.heappop(start_heap)
            # If start_heap is not empty, the top element is the smallest valid right interval.
            if start_heap:
                result[index] = start_heap[0][1]
        return result
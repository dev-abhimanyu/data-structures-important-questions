# https://leetcode.com/problems/merge-sorted-array/description/
import heapq
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        heap = []
        if m != 0:
            heapq.heappush(heap, (temp[0], 1, 0))
        if n != 0:
            heapq.heappush(heap, (nums2[0], 2, 0))
        i = 0
        while len(heap) != 0:
            element, list_index, element_index = heapq.heappop(heap)
            nums1[i] = element
            i += 1
            max_list_size = m if list_index == 1 else n
            if (element_index + 1) < max_list_size:
                if list_index == 1:
                    heapq.heappush(heap, (temp[element_index+1], list_index, element_index+1))
                else:
                    heapq.heappush(heap, (nums2[element_index+1], list_index, element_index+1))
        


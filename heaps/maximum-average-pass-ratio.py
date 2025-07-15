# https://leetcode.com/problems/maximum-average-pass-ratio/
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = []
        # populate the heap with gain, pass and total
        for p, t in classes:
            g = ((p+1)/(t+1)) - p/t
            heapq.heappush(h, (-g, p, t))
        extraStudentsCount = extraStudents
        while extraStudentsCount > 0:
            ng, p, t = heapq.heappop(h)
            p += 1
            t += 1
            g = ((p+1)/(t+1)) - p/t
            heapq.heappush(h, (-g, p, t))
            extraStudentsCount -= 1
        pr_sum = 0.0
        for ng, p, t in h:
            pr_sum += (p/t)
        return pr_sum/len(classes)
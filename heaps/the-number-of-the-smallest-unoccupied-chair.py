# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/
import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        sorted_friends = sorted(enumerate(times), key=lambda x: x[1][0])
        available_chairs = []
        occupied_chairs = []
        chair_index = 0
        for friend_id, (arrival, departure) in sorted_friends:
            # free up the chairs
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                _, chair_number = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, chair_number)
            # assign the chair number
            if available_chairs:
                assigned_chair = heapq.heappop(available_chairs)
            else:
                assigned_chair = chair_index
                chair_index += 1
            # push to occupied chair
            heapq.heappush(occupied_chairs, (departure, assigned_chair))

            # check if it is target friend
            if friend_id == targetFriend:
                return assigned_chair

                    
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        s = sum([abs(seats[i]-students[i]) for i in range(len(seats))])
        return s
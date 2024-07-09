from typing import List
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prev = customers[0][0]
        res = 0
        for arrival, time in customers:
            prep_time = prev
            if arrival >= prep_time:
                prep_time = arrival
            prep_time += time
            res += (prep_time - arrival)
            prev = prep_time
        return res/len(customers)
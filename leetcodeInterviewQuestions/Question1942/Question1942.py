class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chairsAvailable = list(range(len(times))) # Chairs available: 0, 1, ..., n - 1
        heapify(chairsAvailable)

        times = sorted(enumerate(times), key = lambda x : x[1]) # Sort by arrival time with index
        chairsTaken = [] # Will store (time chair becomes vacant, chair number)

        for i, (arrive, leave) in times:
            # Empty all the chairs who should leave before 'arrive'
            while chairsTaken and arrive >= chairsTaken[0][0]:
                heappush(chairsAvailable, heappop(chairsTaken)[1])

            chair_to_sit = heappop(chairsAvailable) # Lowest available chair

            # If the current index is targetFriend, return this chair
            if targetFriend == i: return chair_to_sit

            heappush(chairsTaken, (leave, chair_to_sit))
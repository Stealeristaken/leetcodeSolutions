class Solution:
    def heappeak(self,heap):
        smallest = heapq.heappop(heap)
        heapq.heappush(heap, smallest)
        return smallest[0]
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        heap = []
        free_room = []
        room = [0] * n
        for i in range(n):
            heapq.heappush(free_room,  (0,n - i - 1))

        for i in range(len(meetings)):
            while heap:
                temp = self.heappeak(heap)
                if temp <= meetings[i][0]:
                    x = heapq.heappop(heap)
                    heapq.heappush(free_room,(0,x[-1]))
                else:
                    break
            if free_room:
                x = heapq.heappop(free_room)
            else:
                x = heapq.heappop(heap)
            if x[0] > meetings[i][0]:
                c = x[0] - meetings[i][0]
            else:
                c = 0
            room[x[-1]] += 1
            heapq.heappush(heap, (c + meetings[i][1], x[-1]))
            # print(heap)
        # print(room)
        return room.index(max(room))
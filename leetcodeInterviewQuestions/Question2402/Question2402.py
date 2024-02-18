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
  
  
  
  
  #####################
  
  from heapq import heappop, heappush
from operator import itemgetter

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = list(range(n))
        used_rooms = []
        meetings_per_room = [0] * n
 
        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(available_rooms, room)

            if available_rooms:
                room = heappop(available_rooms)
                heappush(used_rooms, (end, room))
            else:
                room_end, room = heappop(used_rooms)
                room_end += end - start
                heappush(used_rooms, (room_end, room))
            meetings_per_room[room] += 1

        max_index, max_value = max(enumerate(meetings_per_room), key=operator.itemgetter(1))
        return max_index
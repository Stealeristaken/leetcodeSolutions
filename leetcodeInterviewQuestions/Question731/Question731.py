class MyCalendarTwo:

    def __init__(self):
        self.delta = {} 

    def book(self, start: int, end: int) -> bool:
        self.delta[start] = self.delta.get(start, 0) + 1
        self.delta[end] = self.delta.get(end, 0) - 1
        
        active_events = 0
        
        for time in sorted(self.delta):
            active_events += self.delta[time]
            if active_events >= 3:
                self.delta[start] -= 1
                self.delta[end] += 1
                if self.delta[start] == 0:
                    del self.delta[start]
                if self.delta[end] == 0:
                    del self.delta[end]
                return False
            
        return True
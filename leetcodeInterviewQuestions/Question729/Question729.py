class MyCalendar:

    def __init__(self):
        self.start = []
        self.end = dict()

    def book(self, start: int, end: int) -> bool:
        if not self.start:
            self.start = [start]
            self.end[start] = end
            return True

        idx = bisect_right(self.start, start)

        if idx==0:
            if end<=self.start[0]:
                self.start.insert(0, start)
                self.end[start] = end
                return True
            return False

        if idx==len(self.start):
            if self.end[self.start[-1]] <= start:
                self.start.append(start)
                self.end[start] = end
                return True
            return False

        cur = self.start[idx-1]
        if start<=cur or start<self.end[cur] or (idx-1!=len(self.start)-1 and self.start[idx]<end): 
            return False
        self.start.insert(idx, start)
        self.end[start] = end
        return True
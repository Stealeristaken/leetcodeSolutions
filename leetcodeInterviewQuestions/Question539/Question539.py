class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # Convert each time in "HH:MM" format to total minutes and add to the list
        minutes = [self.timeToMinutes(time) for time in timePoints]
        
        # Sort the list of minutes
        minutes.sort()
        
        # Initialize the minimum difference as a large value
        ans = float('inf')
        
        # Calculate the minimum difference between adjacent time points
        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i - 1])
        
        # Consider the wrap-around case between the last and the first time points
        ans = min(ans, 1440 + minutes[0] - minutes[-1])
        
        return ans
    
    # Helper function to convert time "HH:MM" to total minutes
    def timeToMinutes(self, time):
        hour = int(time[:2])
        minute = int(time[3:])
        return hour * 60 + minute
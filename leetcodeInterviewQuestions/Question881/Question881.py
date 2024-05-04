from typing import List 
# This solution is extended time. So wrong in case.
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
            people.sort()
            i, j = 0, len(people) - 1
            count = 0
            while i <= j:
                  if people[i] + people[j] <= limit:
                        i += 1
                        j -= 1
                        count += 1
            return count
      
      
      
#####################

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=0
        people.sort()
        
        while len(people)>2:
            if people[0]+people[-1]<=limit:
                people.pop(0)
                count+=1
            else:
                count+=1
            people.pop(-1)
        if sum(people)<=limit:
            count+=1
        else:
            count+=2

        return count
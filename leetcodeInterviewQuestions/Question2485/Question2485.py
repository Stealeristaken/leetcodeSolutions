##### Binary Search #####
class Solution:
    def pivotInteger(self, n: int) -> int:

        left = 1
        right = n
        
        while(left <= right):

            mid = (left + right) // 2

            # Sum of all the numbers between a and b (including a and b) is (b - a + 1) * (a + b) / 2 

            ps = ((mid - 1 + 1) * (mid + 1)) / 2
            ps1 = ((n - mid + 1) * (mid + n)) / 2

            if(ps == ps1):
                return mid

            # Left sum < right sum
            # So to increase the left sum shift search space towards the right
            elif(ps < ps1):
                left = mid + 1
            
            # Left sum > right sum
            # So to decrease the left sum shift search space towards the left
            else:
                right = mid - 1

        return -1
  
  
  
###### More memory efficient solution ######


class Solution:
    def pivotInteger(self, n: int) -> int:
        flag=0
        x=1
        for x in range(n+1):
            s=0
            a=(x*(x+1))//2
            z=x
            while z!=n+1:
                s=s+z
                z=z+1
            if a==s:
                flag=1
                return x
                break
        if flag==0:
            return -1


        
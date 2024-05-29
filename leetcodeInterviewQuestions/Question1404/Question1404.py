class Solution:
    def numSteps(self, s: str) -> int:
        c = 0
        num = int(s, 2)
        while num != 1:
            if num % 2 == 1:
                num += 1
            else:
                num //= 2
            c += 1
        return c
  
  
  
  
class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0

        binary = list(s)
        
        while len(binary) > 1 or binary[0] != '1':
            if binary[-1] == '0':
                binary.pop()
            else:
                for i in range(len(binary)-1, -1, -1):
                    if binary[i] == '1':
                        binary[i] = '0'
                    else:
                        binary[i] = '1'
                        break
                else:
                    binary.insert(0, '1')
            
            steps += 1
        
        return steps
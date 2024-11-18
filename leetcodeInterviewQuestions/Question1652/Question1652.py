class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        r=[]
        for x in range(len(code)):

            if k>0:
                b=(code[x+1:]+code[:x])[:k]
                r.append(sum(b))
            elif k==0:
                return [0]*len(code)
                
            else:
                #print(k)
                b=((code[:x][::-1])+(code[x+1:][::-1]))[:-k]
                #print(b)
                r.append(sum(b))   



        return r
        
        
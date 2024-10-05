class Solution:
    from collections import Counter 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cs1 = Counter(s1)
        n1 = len(s1)
        n2 = len(s2)
        end = n1 
        flag = False
        temp_cs1 = {}
        # for key,val in cs1.items():
        #     temp_cs1[key] = cs1[key]
        for start in range(n2-n1+1):
            for key,val in cs1.items():
                temp_cs1[key] = cs1[key]   
            for i in range(start,end):
                if s2[i] in temp_cs1.keys():
                    temp_cs1[s2[i]] -= 1
 
            end += 1
            flag = True 
            for j in temp_cs1.values():
                if j != 0:
                    flag = False
            if flag:
                return True 
        return False
            
            
        


        
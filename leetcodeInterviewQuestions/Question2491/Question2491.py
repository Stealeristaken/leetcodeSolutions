class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) %2 != 0: return -1
        if sum(skill) % (len(skill)//2) != 0: return -1

        subsum = sum(skill)//(len(skill)//2)
        sumprod = 0
        count = Counter(skill)
        skill = list(set(skill))
        
        while skill:
            if (subsum - skill[0]) not in skill or count[skill[0]] != count[(subsum - skill[0])]: return -1
            if skill[0] != subsum - skill[0]:
                sumprod += ((skill[0] * (subsum - skill[0])) * count[skill[0]])
            else: sumprod += ((skill[0] * (subsum - skill[0])) * count[skill[0]]//2)
            
            zero = skill[0]
            del skill[0]
            del count[zero]
            if zero != subsum-zero:
                skill.remove(subsum - zero)
                del count[(subsum - zero)]
        
        return sumprod
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res=0
        countPrevious=0
        for i in range(0,(len(bank))):
            countCurrent=bank[i].count('1')
            if (countCurrent>0):
                res+=(countCurrent*countPrevious)
                countPrevious=countCurrent

        return res
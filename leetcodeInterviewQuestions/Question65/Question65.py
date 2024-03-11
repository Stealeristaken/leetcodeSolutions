import re
class Solution:
    def isNumber(self, s: str) -> bool:
        monsterRegex = "(([\+-]?(\d+\.\d+)|[\+-]?(\d+\.)|[\+-]?(\.\d+))|([\+-]?\d+))(e[\+-]?\d+)?"
        if (res := re.search(monsterRegex, s, flags=re.I)) is not None:
            return res.group() == s
        return False
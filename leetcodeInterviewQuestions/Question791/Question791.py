class Solution:
      def customSortString(self, order: str, str: str) -> str:
        count = {}
        for c in str:
            count[c] = count.get(c, 0) + 1
        result = []
        for c in order:
            if c in count:
                result.append(c * count[c])
                count.pop(c)
        for c in count:
            result.append(c * count[c])
        return "".join(result)
  

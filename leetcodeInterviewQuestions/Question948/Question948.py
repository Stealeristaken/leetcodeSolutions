class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        score = 0
        tokens.sort()
        deque = collections.deque(tokens)
        while deque:
            if deque and P >= deque[0]:
                P -= deque.popleft()
                score += 1

            else:
                if len(deque) > 2 and score:
                    P += deque.pop()
                    score -= 1
                else:
                    return score

        return score
  
  
  
  
###############


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        s=0
        m=0
        tokens=sorted(tokens)
        i=0
        j=len(tokens)-1
        while i<=j:
            if power>=tokens[i]:
                power-=tokens[i]
                i+=1
                s+=1
                m=max(m,s)
            elif s>0:
                power+=tokens[j]
                j-=1
                s-=1
            else:
                break
        return m
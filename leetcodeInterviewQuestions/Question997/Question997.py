class Solution:
      def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        trust_score = [0] * (N + 1)
        for a, b in trust:
            trust_score[a] -= 1
            trust_score[b] += 1
        for i in range(1, N + 1):
            if trust_score[i] == N - 1:
                return i
        return -1
  
  
  
  
############################################################################################################



f=open("user.out",'w')
while True:
    try:
        n=int(input())
        trust=input()[2:-2].split('],[')
        trust_him=[1]*(n+1)
        he_trust=[1]*(n+1)
        for i in trust:
            if i=='': break
            i,j=map(int, i.split(','))
            trust_him[j]+=1
            he_trust[i]=0
        ans=-1
        for i in range(1,n+1):
            if he_trust[i] and trust_him[i]==n:
                ans= i
        print(ans,file=f)
    except:
        f.close()
        exit(0)
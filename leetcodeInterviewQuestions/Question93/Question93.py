class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Store all addresses in res
        res = []
        
        def BT(i,address):
            
            # No more digit, so no more state can be generated.
            if i==len(s):
                # It is possible that the address contains less than 4 numbers
                # We only store the valid ones.
                if len(address)==4:
                    res.append( '.'.join(map(str,address)) )
                return
            
            # If the last number is 0, we can add the new digit to it (no leading zero)
            # After adding the new digit, the number has to be <= 255.
            if address[-1]!=0 and address[-1]*10+int(s[i]) <= 255:
                lastItem = address[-1]
                address[-1] = lastItem*10+int(s[i]) #change the current state to its neighboring state
                BT(i+1, address)                    #backtrack(state)
                address[-1] = lastItem              #restore the state (backtrack)
            
            # The address can not contain more than 4 numbers.
            if len(address)<4:
                address.append(int(s[i]))           #change the current state to its neighboring state
                BT(i+1,address)         #backtrack(state)
                address.pop()                       #restore the state (backtrack)
        
        BT(1,[int(s[0])])
        return res
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        op_stack = []
        append_values = '&!|tf'
        operators = '!&|'
        and_or = '&|'
        bools = 'tf'
        bool_convert = {'t': 1, 'f': 0}
        str_convert = {1: 't', 0: 'f'}
        not_convert = {1: 0, 0: 1}

        for e in expression:
            if (e != ')'):
                if (e in append_values):
                    if (e in operators):
                        op_stack.append(e)
                    stack.append(e)
            else:
                curr = -1
                while (stack and stack[-1] != op_stack[-1]):
                    popped = stack.pop()
                    if (popped in bools):
                        popped = bool_convert[popped]
                        if (op_stack[-1] == '!'):
                            curr = not_convert[popped]
                        else:
                            if (curr == -1):
                                curr = popped
                            else:
                                if (op_stack[-1] == '&'):
                                    curr &= popped
                                else:
                                    curr |= popped
                stack.pop()
                stack.append(str_convert[curr])
                op_stack.pop()

        return bool(bool_convert[stack[0]])
class Solution:
    def simplifyPath(self, path):
        stack = []
        path = path.split("/")

        for eleme in path:
            if eleme == "..":
                if stack:
                    stack.pop()
            elif eleme and eleme != ".":
                stack.append(eleme)

        return "/" + "/".join(stack)
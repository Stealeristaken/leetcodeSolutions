class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        first=second=0
        for index, num in enumerate(num1[::-1]):
            first+=(ord(num)-48)*10**index
        for index, num in enumerate(num2[::-1]):
            second+=(ord(num)-48)*10**index

        product=first*second
        answer=''
        while product>0:
            answer=chr(product%10+48)+answer
            product//=10
        return answer if answer !='' else "0"
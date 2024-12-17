class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count_arr = [0 for i in range(26)]

        for c in s:
            count_arr[ord(c) - ord('a')] += 1

        print(count_arr)

        i = 25
        fs = ""
        last_available_index = -1
        while i >= 0:
            if count_arr[i] == 0:
                i -= 1
                continue

            if last_available_index != -1:
                # there is more to be consumed from a greater letter
                # so we will just pick one from this for lexi graphical reasons
                localCount = 1

                # use just one character of i
                count_arr[i] -= 1

                fs += chr(i + ord('a')) * localCount

                # jump back to the greater letter
                i = last_available_index
                last_available_index = -1
            else:
                localCount = min(repeatLimit, count_arr[i])
                count_arr[i] -= localCount

                fs += chr(i + ord('a')) * localCount

                # this can be checked if the count goes to zero but if it goes to zero
                last_available_index = i
                if count_arr[i] == 0:
                    last_available_index = -1
                i -= 1

        return fs
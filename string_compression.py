from collections import Counter
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # Outlier case where chars is one element
        if len(chars) == 1: return 1

        # Make shallow copies
        letter = chars[0]
        copied_chars = chars[1:]

        # Start modifying chars in-place
        chars.clear()
        chars.append(letter)

        consecutive_letter = 1

        for current_letter in copied_chars:
            if current_letter != letter:
                # Append the count only if > 1. Count's digits are split into a list
                if consecutive_letter != 1: chars += [*str(consecutive_letter)]

                chars.append(current_letter)

                # Reset tracking variables
                letter = current_letter
                consecutive_letter = 1
            else:
                consecutive_letter += 1

        # After the for loop, the last letter's count is not yet appended.
        # Again, only append if > 1
        if consecutive_letter != 1: chars += [*str(consecutive_letter)]
        
        return len(chars)


solution = Solution()
print(solution.compress(["a"]))
print(solution.compress(["a","a","b","b","c","c","c"]))
print(solution.compress(["a","a","a","b","b","a","a"]))

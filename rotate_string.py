class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Outlier case where s length > goal length
        if len(s) > len(goal): return False

        s += s
        
        if s.find(goal) == -1:
            return False
        
        return True


solution = Solution()
print(solution.rotateString('abcde', 'cdeab'))
print(solution.rotateString('abcde', 'abced'))
print(solution.rotateString('aa', 'a'))

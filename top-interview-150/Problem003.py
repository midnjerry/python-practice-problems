# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Problem003:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        max = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if (s[j] in charSet):                    
                    break
                else:
                    charSet.add(s[j])
            
            if (len(charSet) > max):
                max = len(charSet)
            
            charSet.clear()
        return max    

if __name__ == '__main__':
    solution = Problem003()    
    print(f'Result (expected 3): {solution.lengthOfLongestSubstring("abcabcbb")}')
    print(f'Result (expected 1): {solution.lengthOfLongestSubstring("bbbbb")}')
    print(f'Result (expected 3): {solution.lengthOfLongestSubstring("pwwkew")}')
    print(f'Result (expected 1): {solution.lengthOfLongestSubstring(" ")}')
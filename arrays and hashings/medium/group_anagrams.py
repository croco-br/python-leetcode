from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}

        for i in range(len(strs)):
            current_value = strs[i]
   
            for j in range(i+1, len(strs)):
                next_value = strs[j]
                if isAnagram(current_value,next_value):
                        results[current_value] += next_value

        return results
    
def isAnagram(s: str, t: str) -> bool:
        if len(s) == 0 or len(t) == 0:
            return False
          
        s1 = ''.join(sorted(s))
        t1 = ''.join(sorted(t))
        
        if s1 == t1:
            return True
        
        return False

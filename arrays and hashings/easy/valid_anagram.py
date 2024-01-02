class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 or len(t) == 0:
            return False
          
        s1 = ''.join(sorted(s))
        t1 = ''.join(sorted(t))
        
        if s1 == t1:
            return True
        
        return False
        
     
       
       
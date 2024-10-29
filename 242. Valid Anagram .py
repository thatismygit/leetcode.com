class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map,t_map=dict(),dict()
        for char in s:
            if char in s_map:
                s_map[char]+=1
                continue
            s_map[char]=1
        for char in t:
            if char in t_map:
                t_map[char]+=1
                continue
            t_map[char]=1
        print(s_map,t_map)
        return s_map==t_map
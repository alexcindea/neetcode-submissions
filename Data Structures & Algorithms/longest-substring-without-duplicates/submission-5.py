class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        hs = set([])
        max_length = 0
        while r < len(s):
            #print(f"start hs: {hs}")
             
            #print(f"curr_length: {curr_length} ")
            
            #print(f"max_length: {max_length}")
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
                #print(hs)
            
            hs.add(s[r])
            curr_length = r - l + 1

            max_length = max(max_length, curr_length)

            #print(hs)
            r += 1

        return max_length

        
class Solution:
    def trap(self, height: List[int]) -> int:
        pref = []
        suff = [0] * len(height)
        

        
        #get max prefixes and suffixes for each i
        pref_max = 0
        for i in range(len(height)):
            pref.append(pref_max)
            if pref_max < height[i]:
                pref_max = height[i]
        
        suff_max = 0
        for i, item in reversed(list(enumerate(height))):
            suff[i] = suff_max
            if suff_max < height[i]:
                suff_max = height[i]
        #print(f"height: {height}")
        #print(f"prefix: {pref}")
        #print(f"suffix: {suff}")

        container = 0
        for i in range(len(height)):
            if(pref[i] == 0 or suff[i] == 0):
                container += 0
                continue
            current_container = min(pref[i], suff[i]) - height[i]
            if current_container < 0:
                current_container = 0
            container += current_container
            #print(f"container for i: {i}, pref[i]: {pref[i]}, suff[i]: {suff[i]}")
            #print(f"container for i: {i}, height[i]: {height[i]}, can hold: {current_container}")
            #print(f"total water {container}")
        

        return container

        
class isAnagram:
    def brute_force(self, s: str, t: str) -> bool:
        # time O(n + m) - space O(n + m)
        s_dict = {}
        t_dict = {}
        for w in s: 
            s_dict[w] = s_dict.get(w, 0) + 1
        for w in t:    
            t_dict[w] = t_dict.get(w, 0) + 1   
        return s_dict == t_dict
    
    def use_sortingclass(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
    def using_hashmap(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
    

    def using_hashTable(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
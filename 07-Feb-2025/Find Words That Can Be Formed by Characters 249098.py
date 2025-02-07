# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        j = Counter(chars)
        cnt=0
        for w in words:
            w_c = Counter(w)

            for c in w:
                if(w_c[c] > j[c]):
                    break
            else:
                cnt+=len(w)
            
        return cnt

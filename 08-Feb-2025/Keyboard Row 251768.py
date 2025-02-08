# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows =[set("qwertyuiop"),set("asdfghjkl"), set("zxcvbnm")]

        cnt =0
        res =[]

        for w in words:
            for r in range(3):
                for c in w:
                    if c.lower() not in rows[r]:
                         break
                else:
                    res.append(w)
                    break
        return res
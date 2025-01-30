# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        new_word =[]

        i =0
        while(i < len(command)):
            ch = command[i]

            if ch=="G":
                new_word.append("G")
            if(ch =="("):
                if(command[i+1] =="a"):
                    i+=2
                    new_word.append("al")
                else:
                    i+=1
                    new_word.append("o")
            i+=1
        return "".join(new_word)

 
# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        #trival case, if columnNumber < 26 return a singer character
        if(columnNumber <=26):
            return chr(ord("A")+columnNumber-1)


        colString =[]
        while(columnNumber>0):
            columnNumber-=1
            rem = columnNumber%26
       
            colString.append(chr((ord("A")+rem)))

            columnNumber//=26

        return "".join(reversed(colString))


 
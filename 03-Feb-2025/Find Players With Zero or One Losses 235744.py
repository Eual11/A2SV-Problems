# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
       match_dict ={} 
       m_count =0 
       for match in matches: 
            m_count = max(m_count, max(match))
            if(match[0] not in match_dict):
                match_dict[match[0]] =0
            if(match[1] not in match_dict):
                match_dict[match[1]]=1
            else:
                match_dict[match[1]]+=1
       print(match_dict) 
       winners = [i for i in match_dict if match_dict[i]==0] 
       losers = [i for i in match_dict if match_dict[i]==1] 
       winners.sort()
       losers.sort()

       return [winners, losers] 
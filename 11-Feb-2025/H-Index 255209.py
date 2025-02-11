# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        if(len(citations) ==1):
            return int(citations[0]!=0)
        h_idx = 0
        citations.sort()

        num_published = 0

        for n in citations:

            total_pub = len(citations)-num_published
            if(n>=total_pub):
                h_idx = max(h_idx, total_pub)
                h_idx= min(len(citations), h_idx)
            num_published+=1


        return h_idx

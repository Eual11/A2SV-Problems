# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        #frankly one of the worst question describtion i have seen in a while
        m, n = len(img), len(img[0])
        res = [[0]*n for _ in range(m)]


        for x in range(m):
            for y in range(n):
                res[x][y] = self.smooth_pixel(img, x, y)

        return res

    # function to apply the image filter
    # 
    def smooth_pixel(self, img, x, y)->int:
        m, n = len(img), len(img[0])
        sum =0
        count =0
        for i in range(-1, 2):
            for j in range(-1, 2):

                xi, yj = x+i, y+j

                if 0<=xi<m and 0<=yj<n:
                    sum+=img[xi][yj]
                    count+=1
                    
        return (sum//count)
                

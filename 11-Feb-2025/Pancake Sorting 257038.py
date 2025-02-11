# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/


        



class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        # fun problem
        # no pancakes for sorted arrays :"")

        def flip(arr, k):

            left =0
            while left < k:
                arr[left], arr[k] = arr[k], arr[left]
                k-=1
                left+=1
        def find_max(arr, n):

            max_idx =0

            for i in range(n):
                if(arr[i] > arr[max_idx]):
                    max_idx =i
            return max_idx

        flip_indies =[]

        n = len(arr)

        while(n > 1):

            m_idx = find_max(arr, n)
            flip_indies.append(m_idx+1)

            if(m_idx != n-1):
                if(m_idx !=0):
                    flip(arr,m_idx)
                flip(arr, n-1)
            flip_indies.append(n)
            n-=1

        print(arr)


        



        return flip_indies

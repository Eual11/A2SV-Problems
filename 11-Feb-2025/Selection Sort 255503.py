# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

#User function Template for python3

class Solution: 
    def selectionSort(self, arr):

        n = len(arr)

        for i in range(n):
        
            min_idx = i
            for j in range(i+1, n):

                if(arr[j] <arr[min_idx]):
                    min_idx = j
            arr[min_idx], arr[i] = arr[i], arr[min_idx]


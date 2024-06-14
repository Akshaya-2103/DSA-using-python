#https://www.geeksforgeeks.org/problems/mirror-tree/1
class Solution:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr

    def missingNumber(self):
        '''for i in range(1,n):
            if i not in arr:
                missing = i
        return missing'''
        s = (n*(n+1))//2
        missing = s - sum(arr)
        return missing

n = int(input())
arr = [int(input()) for i in range(n-1)]
sol = Solution(n, arr)
print(sol.missingNumber())

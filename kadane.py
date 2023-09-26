import sys
from typing import List
class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        sm=0
        mx=-sys.maxsize-1
        n=len(arr)
        
        for i in range(n):
            sm+=arr[i]
            if sm>mx:
                mx=sm
            if sm<0:
                sm=0
            # if mx<0:
            #     mx=0
        return mx
if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    print(Solution().maxSubArray(arr))

            
        
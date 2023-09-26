class Solution:
    def maxProfit(self, arr: list[int]) -> int:
        mx=-9999
        mn=9999
        n=len(arr)
        for i in range(n):
            if mn>arr[i]:
                mn=arr[i]
            if mx<arr[i]-mn:
                mx=arr[i]-mn
        return mx

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    print(Solution().maxProfit(arr))



        
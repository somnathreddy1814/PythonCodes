class Solution:
    def sortColors(self, arr: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n=len(arr)
        low=0
        mid=0
        high=n-1
        while(mid<=high):
            if arr[mid]==0:
                arr[mid],arr[low]=arr[low],arr[mid]
                low+=1
                mid+=1
            elif arr[mid]==2:
                arr[mid],arr[high]=arr[high],arr[mid]
                
                high-=1
            else:
                mid+=1
        return arr

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    print(Solution().sortColors(arr))


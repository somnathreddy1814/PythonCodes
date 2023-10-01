class Item:
    def __init__(self,val,wt):
        self.val=val
        self.wt=wt
class Solution:
    def knapsack(self,n,W,arr):
        arr.sort(key=lambda x:x.val/x.wt , reverse=True)
        curWt=0
        final_val=0.0
        for i in range(n):
            if curWt+arr[i].wt<=W:
                curWt+=arr[i].wt
                final_val+=arr[i].val
            else:
                final_val+=(arr[i].val/arr[i].wt)*(W-curWt)
        return final_val


if __name__=="__main__":
    n=3
    W=50
    arr=[Item(60, 10), Item(100, 20), Item(120, 30)]
    print(Solution().knapsack(n,W,arr))
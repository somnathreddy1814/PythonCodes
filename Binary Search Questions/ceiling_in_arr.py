'''
arr=[2,3,5,9,14,16,18]
target=15

ans-->16
'''
def ceiling(arr,target):
    low=0
    high=len(arr)-1
    res=-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]>=target:
            res=arr[mid]
            high=mid-1
        else:
            low=mid+1
    return res
        
        
    
    
if __name__=="__main__":
    arr=[2,3,5,9,14,16,18]
    target=17
    print(ceiling(arr,target))
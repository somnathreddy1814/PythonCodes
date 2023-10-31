def bs(arr,n,target,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return bs(arr,n,low,mid-1,target)
    elif arr[mid]<target:
        return bs(arr,n,mid+1,high,target)
    # return -1



if __name__=="__main__":
    n=6
    arr=[1,2,3,4,5,6]
    target=4
    print(bs(arr,n,target,0,4))


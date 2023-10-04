def rev(arr,l,r):
    if l>=r: 
        return
    arr[l],arr[r]=arr[r],arr[l]
    rev(arr,l+1,r-1)
    return arr
    


if __name__=="__main__":
    n=5
    arr=[1,2,3,4,5]
    print(rev(arr,0,n-1))
    
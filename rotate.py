def rotate(arr: list, k: int) -> list:
    n=len(arr)
    k=k%n
    if n==0:
        return
    def reverse(start,end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start] 
            start+=1
            end-=1

    reverse(0,n-1)
    reverse(0,n-k-1)
    reverse(n-k,n-1)     
    return arr 



if __name__=="__main__":
    n=5
    arr=[1,2,3,4,5]
    k=3
    #expected=[4,5,1,2,3]
    print(rotate(arr,k))
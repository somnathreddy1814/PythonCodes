def countPlatforms(arr,dept):
    arr.sort()
    dept.sort()
    ans=1
    cnt=1
    i=1
    j=0
    while(i<len(arr) and j<len(dept)):
        if arr[i]<=dept[j]:
            cnt+=1
            i+=1
        else:
            cnt-=1
            j+=1
        ans=max(ans,cnt)
    return cnt


if __name__=="__main__":
    arr = [900, 945, 955, 1100, 1500, 1800]
    dep = [920, 1200, 1130, 1150, 1900, 2000]
    print(countPlatforms(arr, dep))

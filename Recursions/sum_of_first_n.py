def sum(n):
    if n==1:
        return 1
    ans=sum(n-1)
    ans+=n
    return ans



if __name__=="__main__":
    n=3
    print(sum(n))
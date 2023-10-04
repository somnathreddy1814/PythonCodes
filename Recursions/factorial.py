def fact(n):
    if n==1:
        return 1
    ans=fact(n-1)
    ans*=n
    return ans

if __name__=="__main__":
    n=3
    print(fact(n))
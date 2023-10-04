def rev(n):
    if n==0:
        return 
    print(n)
    return(rev(n-1))
    


if __name__=="__main__":
    n=5
    rev(n)
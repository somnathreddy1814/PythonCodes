def repname(n,name):
    if n==0:
        return 
    print(name)
    return repname(n-1,name)

if __name__=="__main__":
    n=5
    name="somnath"
    repname(n,name)
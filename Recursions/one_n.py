
def recur(n):
    if n==1:
        return [1]
    ans=recur(n-1)
    ans.append(n)
    return ans


    

if __name__=="__main__":
    n=5
    print(recur(n))
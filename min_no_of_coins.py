if __name__=="__main__":
    n=int(input())
    lst=[1, 2, 5, 10, 20, 50, 100, 500, 1000]
    res=[]
    for i in range(len(lst)-1,-1,-1):
        if n>=lst[i]:
            n-=lst[i]
            res.append(lst[i])
    print(len(res))
    print(res)


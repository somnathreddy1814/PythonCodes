def fib(n):
    if n<=1:
        return n
    lst=fib(n-1)
    slst=fib(n-2)
    return lst+slst
     


if __name__=="__main__":
    n=2
    print(fib(n))
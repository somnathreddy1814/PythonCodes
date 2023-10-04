def fib(n):
    if n<=1:
        return [n]
    else:
        return [fib(n)+fib(n-1)]

if __name__=="__main__":
    n=5
    print(fib(n))
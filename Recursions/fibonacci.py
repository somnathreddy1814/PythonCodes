
def fib(n):
    if n<2:
        return n
    return fib(n-2)+fib(n-1)
if __name__=="__main__":
    n=5
    print(fib(n))
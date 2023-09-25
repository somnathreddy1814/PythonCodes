from typing import List
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==0:
            return []
        l=[[1]]
        for i in range(n-1):
            new=[1]
            old=l[-1]
            for j in range(len(old)-1):
                v=old[j]+old[j+1]
                new.append(v)
            new.append(1)
            l.append(new)
        return l
if __name__=="__main__":
    n=int(input())
    print(Solution().generate(n))


        
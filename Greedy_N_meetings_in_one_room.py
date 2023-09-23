class meeting:
    def __init__(self,start,end,pos):
        self.start=start
        self.end=end
        self.pos=pos

class solution:
    def maxMeetings(self,s:list[int],e:list[int],n:int)->None:
        meet=[meeting(s[i],e[i],i+1) for i in range(n)]
        sorted(meet,key=lambda x: (x.end,x.pos))
        answer=[]
        limit=meet[0].end
        answer.append(meet[0].pos)
        for i in range(1,n):
            if meet[i].start>limit:
                limit=meet[i].end
                answer.append(meet[i].pos)
        for i in answer:
            print(i,end=" ")
if __name__=="__main__":
    obj=solution()
    n=6
    start=[1,3,0,5,8,5]
    end=[2,4,6,7,9,9]
    obj.maxMeetings(start,end,n)


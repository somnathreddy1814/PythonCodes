class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        llstr = ''
        itr = self.head
        while itr:
            if itr.next:
                llstr += str(itr.data) + "-->"
            else:
                llstr += str(itr.data)
            itr = itr.next
        print(llstr)

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node
    def insert_at_end(self,data):
        node=Node(data,None)
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=node
    def getLen(self):
        cnt=0
        itr=self.head

        while(itr):
            cnt+=1
            itr=itr.next
        return cnt
    def insert_at(self,ind,data):
        itr=self.head
        if ind==0:
            self.insert_at_beg(data)
            return
        
        if ind<0 or ind>self.getLen():
            raise Exception("invalid index")
        cnt=0
        while(itr):
            if cnt==ind-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            cnt+=1
    def remove_at(self,ind):
        if ind<0 or ind>self.getLen():
            raise Exception("invalid index")
        if ind==0:
            self.head=self.head.next
        cnt=0
        itr=self.head
        while(itr):
            if cnt==ind-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            cnt+=1
    def insert_val(self,data):
        self.insert_at_end(data)

        


            
        
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beg("somi")
    ll.insert_at_beg("bhoomi")
    ll.insert_at_end("kami")
    print(LinkedList.getLen(ll))
    ll.insert_at(1,420)
    ll.remove_at(2)
    ll.insert_val(43)

    ll.print()


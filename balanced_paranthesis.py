class Stack():
    def __init__(self):
        self.array=[]

    def insert(self,val):
        self.array.append(val)

    def peek(self):
        return self.array[len(self.array)-1]

    def size(self):
        return len(self.array)

    def values(self):
        return self.array

    def remove(self):
        self.array.pop()


    def bp(self,val):
        if (len(val) % 2 == 0):
            for i in val:
                if i=='(':
                    s.insert(i)
                else:
                    if(s.size()==0):
                        return "nb"
                    else:
                        s.remove()
            if s.size() == 0:
                print "balanced"
        else:
            print "nb"



s=Stack()
s.bp("(()((())()))")







                    
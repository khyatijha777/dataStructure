#stack implementation using arrays
class stack:
    def __init__(self, *args, **kwargs):
        self.s = []
        self.top = -1
    def empty(self):
        if self.top == -1:
            return 1
        else: 
            return 0

    def push(self,x):
        self.top+=1
        self.s.append(x)
        
        
    def pop(self):
        if self.empty():
            print("stack empty")
        else:
            t = self.s[self.top]
            self.s.remove(self.s[self.top])
            self.top-=1
            return t
    def show(self):
        for i in self.s:
            print(i, end = " ")
        print()

if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.show()
    s.pop()
    s.show()
    s.pop()
    s.pop()
    s.show()
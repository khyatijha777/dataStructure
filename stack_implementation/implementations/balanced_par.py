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
        # print("top after pushing: ", self.top)
        
    def pop(self):
        if self.empty():
            print("stack empty")
        else:
            # print("ok")
            t = self.s[self.top]
            # self.s.remove(self.s[self.top])
            self.top -= 1
            # print("top after popping: ", self.top)
            return t
    def show(self):
        for i in self.s:
            print(i, end = " ")
        print()
    def top_el(self):
        return self.s[self.top]
   
def balanced(exp):
    s= stack()
    open_par = ['(', '{', '[']
    closed_par = [')', '}', ']']
    for i in exp:
        if i in open_par:
            
            s.push(i)
            # print("pushing: ", end = "")
            # s.show()
    # s.show()
        if i in closed_par:
            if i == closed_par[open_par.index(s.top_el())] and s.top >= 0:
                # print("popping: ", end = "")
                # s.show()
                s.pop()
            
            else:
                return 0
            
    if s.top == -1:
        return 1
    else:
        return 0

if __name__ == "__main__":
    exp = "{1+2*(2-4)}"
    print("exp : ",exp)
    print(balanced(exp))
    exp = "{1+0]}"
    print("exp : ",exp)
    print(balanced(exp))
    exp = "{1+0{0-0(0}]}"
    print("exp : ",exp)
    print(balanced(exp))
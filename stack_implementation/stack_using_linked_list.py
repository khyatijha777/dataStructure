#stack imlemetation using linked list
class node:
    def __init__(self, x):
        self.val = x
        self.add = None
class stack:
    def __init__(self, *args, **kwargs):
        self.top = node(None)

    def push(self,x):
        new_node = node(x)
        new_node.add =  self.top.add
        self.top.add =new_node

    def pop(self):
        remove = self.top.add
        next_node = remove.add
        self.top.add = next_node
        remove.add = None
        return remove.val

    def empty(self):
        if self.top.add == None:
            return 1
        else:
            return 0

    def show(self):
        curr_node = self.top.add
        while curr_node != None:
            print(curr_node.val, end= " ")
            curr_node = curr_node.add
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
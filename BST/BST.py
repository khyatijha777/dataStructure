
class node:
    def __init__(self, val):
        self.val = val
        self.add1 = None
        self.add2 = None
    
        
class tree:
    def __init__(self):
        self.root =  node(None)

    def search(self,root, x):
        print("root.val : ", root)
        if root== None:
            print("none found")
            return -1
        elif root == x:
            print(" yes found it")
            return 1
    
        elif self.root.val > x:
            self.search(root.add1, x)
        else:
            self.search(root.add2, x)

    def insert( self,x):
        if self.root.val == None:
            self.root.val = x
        else:
            root = self.root
            while True:
            
                if root.val == x :
                    print("already exists")
                    break
                 
                elif x<root.val:
                    if root.add1== None:
                        new_node = node(x)
                        root.add1 = new_node
                        break
                    else:
                        root = root.add1
                else:
                    if root.add2 == None:
                        new_node = node(x)
                        root.add2 = new_node
                        break
                    else:
                        root = root.add2
        

if __name__=="__main__":
    t = tree()
    # q = int(input("enter no of queries"))
    # l = []
    # for i in range(q):
    #     t = input()
    #     l.append(t)
    # for i,j in enumerate(l):
    #     l[i] =  list(j.split(" "))
    #     l[i][1] = int(l[i][1])
    #     if l[i][0]=='i':
    #         insert(l[i][1])
    #     else:
    #         delete(l[i][1])
    t.insert(3)
    t.insert(1)
    t.insert(5)

    # t.insert(1)
    # t.insert(5)

    t.insert(4)
    # t.insert(4)
    # print("root: ", t.root)
    print(t.search( t.root,1))

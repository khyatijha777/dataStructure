#defining the clas of the linked list as ll
class singly_linked_list():
    def __init__(self):
        self.head = node(None)

    def insert_at_beg(self,x):
        print()
        new_node = node(x)
        temp = self.head.next
        self.head.next = new_node
        new_node.next = temp
        print("data: ", new_node.data)
        print("add", new_node.next)

    def print_all_nodes(self):
        cur_node = self.head.next

        while cur_node:
            print("data: ", cur_node.data)
            cur_node = cur_node.next
    
    def insert_at_end(self,x):
        print()
        new_node = node(x)
        cur_node = self.head.next
        #accessing the very last element of the linked list
        pre_node = node(None)
        while cur_node:
            print("data: ", cur_node.data)
            pre_node.next = cur_node
            cur_node = cur_node.next

        pre_node.next = new_node
        new_node.next = None

    def insert_after(self,x,d):
        print()
        
        new_node = node(d)
        cur_node = self.search(x)
        if cur_node == -1:
            return "element not found"
        new_node.next = cur_node.next
        cur_node.next = new_node
        print("insertion done")
             
    def search(self, x):
        cur_node = self.head.next
        count =0
        while cur_node:
            count+=1
            if cur_node.data==x:
                print("found at {} position".format(count))
                return cur_node
            
            cur_node = cur_node.next
        return -1

   

class node():
    def __init__(self, data):
        self.data = data
        self.next = None
    

if __name__=="__main__":
    ll = singly_linked_list()
    ll.insert_at_beg(4)
    ll.insert_at_beg(5)
    ll.insert_at_beg(3)
    ll.print_all_nodes()
    ll.insert_at_beg(7)
    ll.print_all_nodes()
    ll.insert_after(5,6)
    ll.print_all_nodes()
    ll.search(4)


class SLnode:
    def __init__(self,value):
        self.value = value
        self.next = None
class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self,value):
        new_node = SLnode(value)
        #add head  
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return self
    def print_values(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        return self
    def add_to_end(self,value):
        new_node = SLnode(value)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        return self
    def remove_from_front(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None
        return self
    def remove_from_back(self):
        temp = self.head
        pre = temp
        while temp.next:
            pre = temp
            temp= temp.next
        pre.next = None
        return self
    def remove_value(self,value):
        temp = self.head
        pre = None
        if temp is not None and temp.value == value:
            self.remove_from_front()
            return
        while temp is not None and temp.value != value:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        return self

my_list = SList()    # create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_end("fun!")    # chaining, yeah!
my_list.remove_value("are").print_values()
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        return self
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp =temp.next
            temp.next = new_node
            new_node.next= None
            new_node.prev = temp
        return self
    def get(self,index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def delete(self,value):
        temp = self.head
        while temp:
            if temp.value == value:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next
        return self
    def insert(self,index,value):
        new_node = Node(value)
        if index < 0:
            print("wrong Index")
            return False
        if index == 0 :
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None
            self.head = new_node
        if self.get(index).next == None:
            return self.append(value)
        befor = self.get(index-1)
        after = befor.next
        befor.next = new_node
        after.prev = new_node
        new_node.next = after
        new_node.prev = befor
        return self
    
ll = LinkedList()
ll.append(1).append(2).append(3)
ll.delete(3)
ll.print_list()
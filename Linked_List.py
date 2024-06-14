#single linked list

#node has data and address of next node..in linked list
#adress is in hexadecimal..(a456)
#head represent starting node of LL
#head cannot be changed always unneccesarly
#3 usage
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
#Create a LinkedList class
    
# create a linkedlist class
class Linked_List:
    def __init__(self):
        self.head = None

    #Method to add a node at begining of Linked List
    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    #Method to add a node at any index.
    #Indexing starts from 0.
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node

            else:
                print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while(current_node.next != None):
            current_node = current_node.next
        
        current_node.next = new_node

    #Update node of a linked list
    def updateNode(self, data, index):
        current_node = self.head
        position = 0
        while(current_node != None and position != index):
            position = position + 1

    def remove_first_node(self):
        if (self.head == None):
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return
        
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next

        current_node.next = None

    def remove_at_index(self, index):
        if self.head == None:
            return
        
        current_node = self.head
        position = 0
        if(position == index):
            self.remove_first_node()
        else:
            while(current_node.next != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    #Method to remove a node from linked list
    '''def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.remove_first_node()
            return
        
        while (current_node != None and current_node)'''
    
    def sizeOfLL(self):
        size = 0
        if (self.head):
            current_node = self.head
            while(current_node):
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0
        
        #print method ofr the Linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

#create a new linked list
llist = Linked_List()

#add node to the linked list
llist.insertAtEnd("a")
llist.insertAtEnd("b")
llist.insertAtBegin("c")
llist.insertAtIndex('g',1)

print("Node Data")
llist.printLL()

print("\nRemove First Node: ")
llist.remove_first_node()
print("\nRemove Last Node: ")
llist.remove_last_node()
print("Remove at Index: ")
llist.remove_at_index(1)

print("\nLinked List after removinf a node: ")
llist.printLL()

print("\nUpdate node value: ")
llist.updateNode('z',0)
llist.printLL()

print("\nSize of linked list:", end=" ")
print(llist.sizeOfLL())
#Represents the node of list.    
class Node:    
    def __init__(self,data):    
        self.data = data;    
        self.next = None;    
    
class CreateList:    
    #Declaring head and tail pointer as null.    
    def __init__(self):    
        self.head = Node(None);    
        self.tail = Node(None);    
        self.head.next = self.tail;    
        self.tail.next = self.head;    
        
    #This function will add the new node at the end of the list.    
    def add(self,data):    
        newNode = Node(data);    
        #Checks if the list is empty.    
        if self.head.data is None:    
            #If list is empty, both head and tail would point to new node.    
            self.head = newNode;    
            self.tail = newNode;    
            newNode.next = self.head;    
        else:    
            #tail will point to new node.    
            self.tail.next = newNode;    
            #New node will become new tail.    
            self.tail = newNode;    
            #Since, it is circular linked list tail will point to head.    
            self.tail.next = self.head;    
        
    #This function sorts the list in ascending order    
    def sortList(self):    
        #Current will point to head    
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
        else:    
            while(True):    
                #Index will point to node next to current    
                index = current.next;    
                while(index != self.head):    
                    #If current node is greater than index data, swaps the data    
                    if(current.data > index.data):    
                        temp = current.data;    
                        current.data = index.data;    
                        index.data = temp;    
                    index= index.next;    
                current =current.next;    
                if(current.next == self.head):    
                    break;    
                        
    #Displays all the nodes in the list    
    def display(self):    
        current = self.head;    
        if self.head is None:    
            print("List is empty");    
            return;    
        else:    
            #Prints each node by incrementing pointer.    
            print(current.data, end= ' ');    
            while(current.next != self.head):    
                current = current.next;    
                print(current.data,end=' ');    
        print("\n");    
                
class CircularLinkedList:    
    cl = CreateList();    
    #Adds data to the list    
    cl.add(70);    
    cl.add(90);    
    cl.add(20);    
    cl.add(100);    
    cl.add(50);    
        
    #Displaying original list    
    print("Original list: ");    
    cl.display();    
        
    #Sorting list    
    cl.sortList();    
        
    #Displaying sorted list    
    print("Sorted list: ");    
    cl.display();    

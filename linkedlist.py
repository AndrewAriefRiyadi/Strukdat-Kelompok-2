class Node:
    def __init__(self,data):
        self.value = data
        self.next = None

    def setNext(self,Node):
        self.next = Node

    def getNext(self):
        return self.next

    def getValue(self):
        return self.value

    def getIndex(self):
        return


class LinkedList:
    def __init__(self):
        self.first = None
        self.len = 0


    def printList(self):
        temp = self.first
        while (temp):
            if (temp.next == None):
                print(f"{temp.value}  Length: {self.len}")
                break
            else:
                print(temp.value, end=',')
            temp = temp.next
            
    def searchNode(self,index):
        temp = self.first
        for x in range(0,index):
            temp = temp.getNext()
        return temp
        
    def add(self,value):
        temp = Node(value)
        if (self.first == None):
            self.first = temp
        else:
            last = self.first
            while(last.getNext()):
                last = last.getNext()
            last.setNext(temp)
        self.len = self.len + 1


    def insert(self,value,index):
        if(index > self.len-1 or index < 0 ):
            print("Index salah")
            return
        else:
            temp = Node(value)
            if(index == 0):
                temp.setNext(self.first)
                self.first = temp
            else:
                SNode = self.searchNode(index-1)
                temp.setNext(SNode.getNext())
                SNode.next = temp
            self.len = self.len + 1

    def remove(self,index):
        if (index > self.len or index < 0):
            print("Index salah")
            return
        else:
            if (index == 0):
                self.first = self.first.next
            else:
                SNode = self.searchNode(index-1)
                RNode = self.searchNode(index)
                SNode.setNext(RNode.next)
            self.len = self.len - 1

    def swap(self,index1,index2):
        if (index1 > self.len-1 or index1 < 0 or index2 > self.len-1 or index2 < 0):
            print("Index Salah")
            return
        else:
            temp1 = self.searchNode(index1)
            temp2 = self.searchNode(index2)
            self.insert(temp2.getValue(),index1)
            self.remove(index1+1)
            self.insert(temp1.getValue(),index2)
            self.remove(index2+1)

    def removeValue(self,value):
        index = 0
        temp = self.first
        while(temp):
            if(temp.getValue() == value):
                if (index == 0):
                    self.first = self.first.next
                    self.len -= 1
                    index -= 1
                else:
                    SNode = self.searchNode(index-1)
                    SNode.setNext(temp.next)
                    self.len -= 1
                    index -= 1
            temp = temp.getNext()
            index += 1


    def removeDup(self):
        temp1 = self.first
        index1 = 0
        index2= index1+1
        while(temp1):
            temp2 = temp1.next
            while(temp2):
                if(temp1.getValue() == temp2.getValue()):
                    self.remove(index2)
                temp2 = temp2.next
                index2 += 1
            temp1 = temp1.next
            index1 += 1
            index2 = index1+1

    def tailToFront(self):
        self.swap(0,self.len-1)

if __name__ == '__main__':
    list = LinkedList()
    list.add(5)
    list.add(23)
    list.add(17)
    list.add(7)
    list.add(2)
    list.add(28)
    list.add(13)
    list.add(7)
    list.add(23)
    list.printList()
    list.removeValue(2)
    list.printList()
    list.removeDup()
    list.printList()
    list.tailToFront()
    list.printList()


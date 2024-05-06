class node:
    def __init__(self,root):
        self.data=root
        self.left=None
        self.right=None

    def insert(self, value):
        if self.data == value:
            return
        if self.data>value:
            if self.left:
                self.left.insert(value)
            else:
                self.left=node(value)
        if self.data<value:
            if self.right:
                self.right.insert(value)
            else:
                self.right=node(value)

    def show(self):
        if self:
            if self.left:
                self.left.show()
            print(self.data,end=" -> ")
            if self.right:
                self.right.show()

    def search(self, value):
        if self.data == value:
            print("\n\n[*] Your value is found in tree", self.data)
            return
        elif self.data > value:
            if self.left:
                self.left.search(value)
            else:
                print("\n\n[!] Value not found in tree.")
        else:
            if self.right:
                self.right.search(value)
            else:
                print("\n\n[!] Value not found in tree.")
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.data 
        
    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self.data







a=node(17)
a.insert(4)
a.insert(12)
a.insert(15)
a.insert(18)
a.insert(22)
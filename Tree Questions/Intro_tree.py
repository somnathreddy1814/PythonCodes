class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)
        
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self):
        spaces=' '*self.get_level()*3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
def build_product_tree():
    root=TreeNode("Electronics")

    laptop=TreeNode("Laptop")
    root.add_child(laptop)
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Think pad"))
    laptop.add_child(TreeNode("Surface"))

    tv=TreeNode("TV")
    root.add_child(tv)
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samsung"))

    mobile=TreeNode("Mobile")
    root.add_child(mobile)
    mobile.add_child(TreeNode("Samsung"))
    mobile.add_child(TreeNode("Pixel"))
    








    root.print_tree()

if __name__=="__main__":
    build_product_tree()
    
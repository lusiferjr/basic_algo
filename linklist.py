class node:
    def __init__(self,data=None):
        self.data=data
        self.nextPointer=None

class linklist:
    def __init__(self):
        self.nodes=[]
        self.first=None
    def newnode(self,a):
        if self.nodes.__len__()==0:
            temp=node(a)
            self.first=temp
            self.nodes.append(temp)
        else:
            temp=node(a)
            self.nodes.append(temp)
            self.nodes[self.nodes.__len__()].nextPointer=temp
    def itter(self):
        cur_node=self.first
        while(cur_node.nextPointer!=None)
        {
            print(cur_node.data)
            cur_node=cur_node.nextPointer
        }
        print(cur_node.data)
    def dell(self,a):
        cur_node=self.first
        while cur_node.nextPointer=None:
            if cur_node.data=a:
                if slef.nodes[0]=cur_node:
                    self.first=cur_node.nextPointer
            self.nodes.remove(cur_node)


# root=node(0)
# a=root
# for i in range(1,11):
#     n=node(i)
#     a.nextPointer=n
#     a=n
# a=root
# # while a.nextPointer!=None :
# #     print(a.data)
# #     a=a.nextPointer
# while a.nextPointer!=None:
#     if a.data==4:
#         a=a.nextPointer
#         root=a
#     if a.nextPointer.data==4 :
#         a.nextPointer=a.nextPointer.nextPointer
#         break
#     a=a.nextPointer
# a=root
# while a.nextPointer!=None :
#     print(a.data)
#     a=a.nextPointer


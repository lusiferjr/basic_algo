class node:
    def __init__(self,value):
        self.value=value
        self.list=[]
class edge:
    def __init__(self,a,b,w):
        self.value=w
        self.a=a
        self.b=b
    def addedge(self,t):
        self.a.list.append(t)
        self.b.list.append(t)
class graph:
    def __init__(self):
        self.nodes=[]
        self.edges=[]
    def addnode(self,a):#add a new node in graph
        self.nodes.append(node(a))
    def addedge(self,a,b,w):#add a new edge between two nodes
        temp1=None
        temp2=None
        for i in self.nodes:
            if i.value==a:
                temp1=i
            elif i.value==b:
                temp2=i
        temp=edge(temp1,temp2,w)
        self.edges.append(temp)
        temp.addedge(temp)
    def dell(self,a):#dellete a node from graph
        try:
            for i in self.nodes:
                if i.value==a:
                    self.nodes.remove(i)
                    for j in i.list:
                        temp=j.a
                        if temp==i:
                            temp=j.b
                        temp.list.remove(j)
                    break
        except:
            print("entered node was never created")
    def itt(self):#traverse the graph 
        for i in self.nodes:
            print(i.value,"==>",end="")
            for j in i.list:
                temp=j.a
                if temp==i:
                    temp=j.b
                print('connect to {}'.format(temp.value),'\t','weight {}'.format(j.value))
    def ittnode(self,a):#traverse a particular node
        temp=None
        for i in self.nodes:
            if i.value==a:
                temp=i
                break
        print(temp.value,"==>",end="")
        for j in temp.list:
            temp=j.a
            if temp==i:
                temp=j.b
            print('\tconnect to {}'.format(temp.value),'\t','weight {}'.format(j.value),end='\n')       
    def dellW(self,a,b,w):#delete a edge between two node with gievn weight
        try:
            for i in self.edges:
                if i.a.value==a and i.b.value==b:
                    if i.value==w:
                        self.edges.remove(i)
                        i.a.list.remove(i)
                        i.b.list.remove(i)
                        break
                elif i.a.value==b and i.b.value==a:
                    if i.value==w:
                        self.edges.remove(i)
                        i.a.list.remove(i)
                        i.b.list.remove(i)
                        break
        except:
            print("no edge connecting")
    def dijkstra(self,a):
        node=None
        disc={}
        temp=[]
        for i in self.nodes:
            if i.value=a:
                node=i
            else :
                disc[i.value]=[]
        for i in node.list:
            conto=None
            if i.a.value=a:
                conto=i.b.value
            else:
                conto=i.a.value
            

            
        


class node:
    _nodeData = None
    _nextNode = None

    def __init__(self, data):
        self._nodeData = data

    def setNextNode(self, node):
        self._nextNode = node

    def getNextNode(self):
        return self._nextNode

    def getData(self):
        return self._nodeData

    def setData(self, data):
        self._nodeData = data

class linkedList:

    _firstNode = None
    
    def __init__(self, data):
        self._firstNode = node(data)

    def findLastNode(self, node):
        link = node.getNextNode()
        return node if link == None else self.findLastNode(link)

    def addNode(self, data):
        self.findLastNode(self._firstNode).setNextNode(node(data))

    def findNode(num):
        return _findNode(_firstNode, num, 0)
        
    def _findNode(node, num, i):
        if node == None or num < 0: raise IndexError
        return node.getData() if num == i else _findNode(node.getNextNode(), data, i+1) 
        
    def deleteNode(self, num):
        if num == 0: self._firstNode = self._firstNode.getNextNode()
        else:
            prevNode = _findNode(self._firstNode, num-1, 0)
            prevNode.setNextNode(prevNode.getNextNode().getNextNode() if prevNode.getNextNode() != None else None) 

    def printAllNodes(self, node):
        return "'" + str(node.getData()) + "', " + (self.printAllNodes(node.getNextNode()) if node.getNextNode() !=None else "")
    
    def __str__(self):
        allNodes = self.printAllNodes(self._firstNode)
        allNodes = allNodes[:len(allNodes)-2]
        return "["+allNodes+"]"
        
newList = linkedList("Pisyunin")
newList.addNode("Pidor")
newList.addNode("Azaza")
newList.addNode("Paskhalochka :)")
print(newList)
    

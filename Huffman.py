import heapq
class Node:

    def __init__(self,freq,symbol,left=0,right=0):
        self.freq=freq
        self.symbol=symbol
        self.left=left
        self.right=right
        self.huff=""

    def __lt__(self,nxt):
        return self.freq<nxt.freq
    
def printNodes(node,val=""):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left,newVal)

    if node.right:
        printNodes(node.right,newVal)

    if not node.left and not node.right:
        print(f"{node.symbol}->{newVal}")

chars=['a','b','c','d','e']
freq=[0.22,0.34,0.17,0.19,0.08]

nodes=[]

for i in range(len(chars)):
    heapq.heappush(nodes,Node(freq[i],chars[i]))

while len(nodes)>1:
    left=heapq.heappop(nodes)
    right=heapq.heappop(nodes)

    left.huff=0
    right.huff=1

    newNode=Node(left.freq+right.freq,left.symbol+right.symbol,left,right)
    heapq.heappush(nodes,newNode)

print("Huffman Codes: ")
printNodes(nodes[0])

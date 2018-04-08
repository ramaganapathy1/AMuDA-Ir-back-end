#!/usr/bin/python

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val
        self.depth = 0

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def addroot(self, val):
        if(self.root == None):
            self.root = Node(val)

    def add(self, key, val):
        toAdd = self.find(key)
        if (toAdd != None):
            if len(val) == 1:
                toAdd.l = Node(val[0])
            elif len(val) > 1:
                toAdd.l = Node(val[0])
                toAdd.r = Node(val[1])


    def find(self, key):
        if(self.root != None):
            return self._find(key, self.root)
        else:
            return None

    def _find(self, key, node):
        if(key == node.v):
            return node
        else:
            if(node.l != None):
                toRet = self._find(key, node.l)
                if(toRet != None):
                    return toRet
                else:
                    if(node.r != None):
                        toRet = self._find(key, node.r)
                        if(toRet != None):
                            return toRet

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print str(node.v)
            self._printTree(node.r)

    def height(self, node) :
        if(node==None):
            return 0
        else:
           lDepth = self.height(node.l)
           rDepth = self.height(node.r)
           if (lDepth > rDepth):
               return(lDepth+1)
           else:
               return(rDepth+1)

    def traverse(self, rootnode):
        thislevel = [rootnode]
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                start = ""
                self.caldepth(self.root,0)
                for i in range(n.depth):
                    start += "-"
                print start,n.v
                if n.l: nextlevel.append(n.l)
                if n.r: nextlevel.append(n.r)
            print
            thislevel = nextlevel

    def prettyprint(self, node, start, fdout):
        if(node.l != None):
            print start+str(node.l.v)
            fdout.write(start+str(node.l.v)+"\n")
            self.prettyprint(node.l,"    "+start, fdout)
            if(node.r != None):
                print start+str(node.r.v)
                fdout.write(start+str(node.l.v)+"\n")
                self.prettyprint(node.r,"    "+start, fdout)

    def caldepth(self, node, depth):
        if node != None:
            node.depth = depth
            self.caldepth(node.l, depth+1)
            self.caldepth(node.r, depth+1)
"""
#     3
# 0     4
#   2      8
tree = Tree()
tree.addroot(4)
tree.add(4,[2,6])
tree.add(2,[1,3])
tree.add(6,[5,7])
tree.add(1,[8])
tree.printTree()
print "#############find"
print (tree.find(3)).v
print "#############height"
print tree.height(tree.root)
print "#############traverse"
tree.traverse(tree.root)
tree.caldepth(tree.root, 0)
print "#############pretty"
print tree.root.v
tree.prettyprint(tree.root,"||")
"""

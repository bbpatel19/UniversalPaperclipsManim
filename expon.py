
import numpy as np


def binaryTree(depth, options = 2, scale = 1, highesty = 3.5, xrange = 14):
    vertices = ["vertex_0_0"]
    edges = []

    for j in range(depth):
        for i in range(0, np.power(options, j) - 1, options):
            for o in range(options):
                vertices.append("vertex_%i_%i" % (j, i + o))
                edges.append(("vertex_%i_%i" % (j - 1, np.floor(i / options)), "vertex_%i_%i" % (j, i + o)))
        
    def vertToCoord(vertex_0_0):
        vertex = vertex_0_0.split("_")
        layer = float(vertex[1])
        posin = float(vertex[2])
        ypos = highesty - 1.75 * highesty * np.log10(1 + layer)
        xpos = (posin + 1) * xrange / (1 + np.power(options, layer)) - xrange / 2
        return [xpos, ypos, 0]


    
    graphs = []
    lvertices = []
    ledges = []
    for k in range(depth, depth + 1):
        for l in vertices:
            if l.split("_")[1] == str(k - 1) or l.split("_")[1] == str(k - 2):
                lvertices.append(l)
        for l in edges:
            if l[0].split("_")[1] == str(k - 2):
                ledges.append(l)
        #G = Graph(lvertices, ledges)
        #G.scale(scale)
        #for i in lvertices:
        #    G[i].move_to(vertToCoord(i))
        #graphs.append(G)
        print(lvertices)
        print(ledges)
    
    #return graphs

binaryTree(depth = 2, options = 3, scale = 1)

#exponentialGrowth animation
from manim import *

#custom made babyyyyyyyyy. I had tooo much fun with this babyyyyyyyyyyyyyyy
#what the hell is this. what the actual h e double hockeysticks is this
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
    for k in range(depth + 1):
        lvertices = []
        ledges = []
        for l in vertices:
            if l.split("_")[1] == str(k - 1) or l.split("_")[1] == str(k - 2):
                lvertices.append(l)
        for l in edges:
            if l[0].split("_")[1] == str(k - 2):
                ledges.append(l)
        G = Graph(lvertices, ledges)
        G.scale(scale)
        for i in lvertices:
            G[i].move_to(vertToCoord(i))
        graphs.append(G)
        
    return graphs
        
class tree2(Scene):
    def construct(self):        
        probe = ImageMobject("media/assets/ProbePNG.png")
        probe.move_to([0, 3.5, 0])
        probe.z_index = 1
        self.wait()
        self.play(FadeIn(probe))
        
        depths = 7
        option = 2
        scaling = 0.75
        gTree = binaryTree(depth = depths, options = option, scale = scaling)
        
        anims = [Create(gTree[i]) for i in range(2, depths + 1)]
        self.wait(2)
        for l in range(len(anims)):
            self.play(anims[l])
            self.wait(2)

class tree3(Scene):
    def construct(self):
        depths = 5
        option = 3
        scaling = 0.75
        gTree = binaryTree(depth = depths, options = option, scale = scaling)
        
        anims = [Create(gTree[i]) for i in range(2, depths + 1)]
        self.wait(2)
        for l in range(len(anims)):
            self.play(anims[l])
            self.wait(2)

import networkx as nx
class tree4(Scene):
    def construct(self):
        G = nx.generators.balanced_tree(5,3)
        g4 = Graph(list(G.nodes), list(G.edges), layout = "kamada_kawai").scale(1.5)
        self.wait()
        self.play(Create(g4), run_time = 10)
        self.wait()

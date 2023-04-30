
#import networkx as nx
#G = nx.generators.balanced_tree(2,5)
#print(list(G.nodes))
#print("value%i %i" % (5,4))


#work on edges
#from colour import *
#cl = 0.1 / 360
#print(Color(hsl = (cl, 1, 0.5)))
import numpy as np



"""
qchipnew = [lambda x, n = i: 360 * np.sin((1 + n) * x / 10) for i in range(10)]

def qchip1(x):
    return 360 * np.sin(x*1/10)
def qchip2(x):
    return 360 * np.sin(x*2/10)
def qchip3(x):
    return 360 * np.sin(x*3/10)
def qchip4(x):
    return 360 * np.sin(x*4/10)
def qchip5(x):
    return 360 * np.sin(x*5/10)
def qchip6(x):
    return 360 * np.sin(x*6/10)
def qchip7(x):
    return 360 * np.sin(x*7/10)
def qchip8(x):
    return 360 * np.sin(x*8/10)
def qchip9(x):
    return 360 * np.sin(x*9/10)
def qchip10(x):
    return 360 * np.sin(x*10/10)
qchip = [qchip1, qchip2, qchip3, qchip4, qchip5, qchip6, qchip7, qchip8, qchip9, qchip10]

print(qchip[3](2))
print(qchipnew[3](2))
"""


"""
def fun1(x):
    return lambda w, z: 2*x+w

print(fun1(1)(3))
"""


"""
x = [[1,2,3], [2, 3, 0], [1, 0 , -1]]

for list in x:
    for i in range(len(list)):
        list[i] *= 3
print(x)
"""

"""
def vertToCoord(vertex_0_0):
    vertex = vertex_0_0.split("_")
    return [float(vertex[1]), float(vertex[2]), 0]

print(vertToCoord("vertex_1_3"))
"""



"""
import numpy as np
vertices = ["vertex_0_0"]
edges = []

for j in range(4):
    for i in range(0, np.power(2, j) - 1, 2):
        vertices.append("vertex_%i_%i" % (j, i))
        if j == 0:
            continue
        vertices.append("vertex_%i_%i" % (j, i + 1))
        edges.append(("vertex_%i_%i" % (j - 1, np.floor(i / 2)), "vertex_%i_%i" % (j, i)))
        edges.append(("vertex_%i_%i" % (j - 1, np.floor(i / 2)), "vertex_%i_%i" % (j, i + 1)))


for k in range(len(vertices)):
    print("%s " %(vertices[k]))

for k in range(len(edges)):
    print(edges[k])
"""
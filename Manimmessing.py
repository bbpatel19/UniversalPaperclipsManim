from manim import *
#relevant video
#https://youtu.be/1Fv0Nu-Tb7Q?list=PLsMrDyoG1sZm6-jIUQCgN3BVyEVOZz3LQ

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class basicGroups(Scene):
    def construct(self):
        circle = Circle(radius = 0.2, color = PINK, fill_opacity = 0.5)
        circles = VGroup(*[circle.copy() for _ in range(20)])
        circles.arrange_in_grid(4,5)
        self.add(circles)


class basicAnimations(Scene):
    def construct(self):
        sq = Square(side_length = 0.2, color = PINK, fill_opacity = 0.5)
        self.play(sq.animate.shift(RIGHT))
        self.play(sq.animate(run_time = 2).scale(3))
        self.play(sq.animate().scale(1/2).shift(2*LEFT))
        ci = Circle(radius = 0.2, color = PURPLE, fill_opacity = 0.5)
        self.add(ci)
        self.play(VGroup(sq,ci).animate.arrange(RIGHT))

import networkx as nx
class exampletree(Scene):
    def construct(self):
        G = nx.Graph()

        G.add_node("ROOT")

        for i in range(5):
            G.add_node("Child_%i" % i)
            G.add_node("Grandchild_%i" % i)
            G.add_node("Greatgrandchild_%i" % i)

            G.add_edge("ROOT", "Child_%i" % i)
            G.add_edge("Child_%i" % i, "Grandchild_%i" % i)
            G.add_edge("Grandchild_%i" % i, "Greatgrandchild_%i" % i)
        
        self.play(Create(Graph(list(G.nodes), list(G.edges), layout = "tree", root_vertex = "ROOT")))

class graphexample(Scene):
    def construct(self):
        vertices = [1,2,3,4,5,6,7]
        edges = [(1,2), (1,3), (2,4), (2,5), (3,6), (3,7)]
        g = Graph(vertices, edges)
        self.play(Create(g))
        self.wait()
        self.play(
            g[1].animate.move_to([0,3,0]),
            g[2].animate.move_to([1,2,0]),
            g[3].animate.move_to([-1,2,0]),
            g[4].animate.move_to([1.5,1,0]),
            g[5].animate.move_to([0.5,1,0]),
            g[6].animate.move_to([-0.5,1,0]),
            g[7].animate.move_to([-1.5,1,0]),
        )
        self.wait()

class meeting(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()
        dot_1 = Dot3D(point = axes.c2p(0, 0, 1), color = RED)
        dot_2 = Dot3D(point = axes.c2p(2, 0, 1), radius = 0.1, color = BLUE)
        dot_3 = Dot3D(point = axes.c2p(0, 0, 0), radius = 0.1, color = ORANGE)

        self.add(axes, dot_1, dot_2, dot_3)
        self.begin_ambient_camera_rotation(rate = 1)
        self.wait(5)


#how to use colors
"""
for i in vertTrun:
            dot = Dot3D(point = i, color = Color(hsl = (i[2] * 75 / 360, 1, 0.5)))
            self.add(dot)
"""

class testing(Scene):
    def construct(self):
        dot = Dot()
        self.add(dot)
        self.wait()
        dot.shift(UP)
        self.add(dot)
        self.wait()



#base File
#for running
#py -m manim render -pql [filename] [resultname]
# or smth of that nature
#then the rest is history isn't it :)
#cd .\Desktop\SilverRepose\vscodethign\
#py -m manim render -pql manimmessing.py
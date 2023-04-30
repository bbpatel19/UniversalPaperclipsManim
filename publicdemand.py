#public demand animation
from manim import *

class publicDemand(Scene):
    def construct(self):
        graph = Axes(
            x_range=[1,20], 
            y_range=[0,1],
            x_axis_config={
                "numbers_to_include": [1,5,10,15,20],
                "numbers_with_elongated_ticks": [1,5,10,15,20]
            },
            tips = False
            )
        self.add(graph)
        graph2 = Axes(
            x_range=[1,7],
            y_range=[0,1],
            x_axis_config={
            "numbers_to_include": [1,2,3,4,5,6,7],
            "numbers_with_elongated_ticks": [1,3,5,7]
            },
            tips = False
        )
        
        def pd(x):
            return 0.8 / x
        
        pdgraph = graph.plot(pd, color = BLUE)
        pdgraph2 = graph2.plot(pd, color = BLUE)
        self.wait()
        self.play(Create(pdgraph), run_time = 2)
        self.wait()

        t = ValueTracker(15)
        dot = Dot(point = [graph.coords_to_point(t.get_value(), pd(t.get_value()))])

        dot2initial = [graph2.coords_to_point(t.get_value(), pd(t.get_value()))]
        dot2 = Dot(point = dot2initial)
        dot.add_updater(lambda x: x.move_to(graph2.c2p(t.get_value(), pd(t.get_value()))))

        
        self.add(dot)
        self.wait()
        self.play(Transform(graph, graph2), Transform(pdgraph, pdgraph2), Transform(dot, dot2))
        self.wait()
        self.play(t.animate.set_value(3))
        self.wait()
        self.play(t.animate.set_value(1))
        self.wait()
        self.play(t.animate.set_value(5))



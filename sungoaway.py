#the mask for the sun go away

from manim import *

class sunmask(Scene):
    def construct(self):
        ci = Circle(radius = 0, color = GREEN)
        ci.set_fill(GREEN, opacity = 1)
        cigoal = Circle(radius = 3.5, color = GREEN)
        cigoal.set_fill(GREEN, opacity = 1)
        self.add(cigoal)
        self.wait()
        self.play(Transform(cigoal, ci), run_time = 3 * 60 + 15)
        self.wait()
        
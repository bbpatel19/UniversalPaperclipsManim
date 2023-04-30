#quantum computing number of operations animation

#could come back and add the quantum chips

from manim import *

class quantum(Scene):
    def construct(self):
        #axes
        ax = Axes(
            x_range = [0, 20 * np.pi , np.pi], 
            y_range = [0, 2750, 250], 
            x_axis_config={
            }, 
            y_axis_config={
            "numbers_to_include": np.arange(0,2751,250)
            #"unit_size": 250
            }, 
            tips = False
            )
        self.add(ax)

        #individual chip functions
        qchip = [lambda x, n = i: 360 * np.sin((1 + n) * x / 10) for i in range(10)]
        def qchiptotal(x,n):
            y = 0
            for i in range(n):
                y += qchip[i](x)
            return y
        #total chip functions
        qchiptot = [lambda x, n = i: qchiptotal(x, n + 1) for i in range(10)]
        #graphs individual chip functions
        qqgraphs = [ax.plot(qchip[i], color = BLUE, stroke_width = 1.4) for i in range(10)]
        #graphs total chip functions
        qqgraphstot = [ax.plot(qchiptot[i], color = RED, stroke_width = 1.4) for i in range(10)]
        
        #animations
        anims = []
        for i in range(10):
            anims.append(Create(qqgraphs[i]))
            anims.append(ReplacementTransform(qqgraphs[i], qqgraphstot[i]))
            if i == 0:
                continue
            anims.append(ReplacementTransform(qqgraphstot[i-1], qqgraphstot[i]))
            anims.append(FadeOut(qqgraphstot[i-1], run_time = 0.1))

        #actual chips
        t = ValueTracker(0)
        sq = [Square(side_length = 1, color = WHITE) for i in range(10)]
        for i in range(len(sq)):
            sq[i].add_updater(lambda square, n = i: square.set_fill(WHITE, opacity = np.sin((n + 1) / 10 * t.get_value())))
            sq[i].move_to([-5, 3, 0])
            if i != 0:
                sq[i].next_to(sq[i-1], RIGHT)

        #playing the graph animations
        time = 0.5
        self.wait()
        self.play(anims[0], Create(sq[0]), run_time = time)
        self.play(anims[1])
        for i in range(2, len(anims), 4):
            self.play(anims[i], Create(sq[1 + int(i / 4)]), run_time = time)
            self.play(AnimationGroup(anims[i+2], anims[i+1], lag_ratio = 0.1))
            self.play(anims[i+3])

        #moving dot animations + quantum chips
        dot = Dot(point = ax.c2p(0, qchiptot[9](0)), color = RED_A)
        self.add(dot)
        dot.add_updater(lambda generic: generic.move_to(ax.c2p(t.get_value(), qchiptot[9](t.get_value()))))
        self.play(t.animate.set_value(6), run_time = 2)
        self.play(sq[9].animate.move_to(ORIGIN - DOWN))
        self.play(t.animate.set_value(20 * np.pi), run_time = 33, rate_function = "linear")
        self.wait()

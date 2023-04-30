#yomi

from manim import *

class tableyomi(Scene):
    def construct(self):
        #base for table
        sq = Rectangle(color = WHITE, height = 2, width = 4, grid_xstep = 2, grid_ystep = 1)
        
        #the As and Bs on the side of the table
        optiona = Text('A')
        optionb = Text('B')
        optiona1 = optiona.copy()
        optionb1 = optionb.copy()
        optiona1.shift(LEFT + 3/2 * UP)
        optionb1.shift(RIGHT + 3/2 * UP)
        optiona.shift(1/2 * UP + 5/2 * LEFT )
        optionb.shift(1/2 * DOWN + 5/2 * LEFT)

        #the text of the table
        strategya = Text('A100')
        strategyb = Text('B100')
        payoutaa =  Text('3, 3')
        payoutab =  Text('4, 5')
        payoutba =  Text('5, 4')
        payoutbb =  Text('6, 6')
        strategya.shift(UP * 5/2) 
        strategyb.shift(LEFT * 4)
        payoutaa.shift(LEFT + 1/2 * UP)
        payoutab.shift(RIGHT + 1/2 * UP)
        payoutba.shift(LEFT + 1/2 * DOWN)
        payoutbb.shift(RIGHT + 1/2 * DOWN)
        
        #animating the creation of table
        table = [optiona, optionb, optiona1, optionb1, strategya, strategyb, payoutaa, payoutab, payoutba, payoutbb]
        tableMake = [Create(sq, run_time = 2)]
        for i in range(len(table)):
            tableMake.append(Write(table[i], run_time = 2))
        self.play(AnimationGroup(*tableMake))
        self.wait()
        
        #animating the winning of the table
        wina = Text('5').move_to(payoutba)
        wina.align_to(payoutba, LEFT)
        winb = Text('4').move_to(payoutba)
        winb.align_to(payoutba, RIGHT)
        winRepresent = AnimationGroup(wina.animate.next_to(strategya, UP), winb.animate.next_to(strategyb, UP))
        self.play(AnimationGroup(Indicate(payoutba, run_time = 1.8), winRepresent, lag_ratio = 0.10))
        self.play(FadeOut(wina), FadeOut(winb))
        self.wait()

        #Swap Strategies example + b always choose b a choose a
        self.play(Transform(strategya, Text('B100').align_to(strategya, UP)), Transform(strategyb, Text('A100').align_to(strategyb, LEFT)))
        self.wait()
        self.play(Indicate(payoutab), run_time = 1.3)
        self.wait(0.2)
        self.play(Indicate(strategya), Indicate(optionb1), run_time = 1.3)
        self.wait(0.2)
        self.play(Indicate(strategyb), Indicate(optiona), run_time = 1.3)
        self.wait(0.2)

        #animating winning of swapped table        
        wina.move_to(payoutab)
        wina.align_to(payoutab, RIGHT)
        winb.move_to(payoutab)
        winb.align_to(payoutab, LEFT)
        winRepresent2 = AnimationGroup(wina.animate.next_to(strategya, UP), winb.animate.next_to(strategyb, UP))
        self.play(AnimationGroup(Indicate(payoutab, run_time = 1.8), winRepresent2, lag_ratio = 0.10))
        self.play(FadeOut(wina), FadeOut(winb))
        self.wait()
        
        #animation for the new table
        tableTransform = AnimationGroup(
            Transform(payoutaa, Text('8, 8').move_to(payoutaa)),
            Transform(payoutab, Text('3, 10').move_to(payoutab)),
            Transform(payoutba, Text('10, 3').move_to(payoutba)),
            Transform(payoutbb, Text('4, 4').move_to(payoutbb)),
            Transform(strategya, Text('A100').move_to(strategya)),
            Transform(strategyb, Text('A100').move_to(strategyb))
        )
        self.play(tableTransform)
        self.wait(6)
        self.play(AnimationGroup(Indicate(VGroup(optiona, strategyb), run_time = 1.6), Indicate(VGroup(optiona1, strategya), run_time = 1.6), Indicate(payoutaa, run_time = 1.8), lag_ratio = 0.75))
        self.wait()

        #animation of rest of different kind of strategies
        strategyTransform = [
            Transform(strategya, Text('Random').move_to(strategya)),
            Transform(strategyb, Text('Greedy').move_to(strategyb)),
            Transform(strategya, Text('Generous').move_to(strategya)),
            Transform(strategyb, Text('MinMax').move_to(strategyb)),
            Transform(strategya, Text('TitforTat').move_to(strategya)),
            Transform(strategyb, Text('BeatLast').move_to(strategyb)),
        ]
        for i in range(0, len(strategyTransform) - 1, 2):
            self.play(AnimationGroup(strategyTransform[i], strategyTransform[i+1], lag_ratio = 0.1))
            self.wait(0.4)
        self.wait()
        
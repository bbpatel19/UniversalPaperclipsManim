#This is the old ending cutscene i was working on.
#it still has some useful stuff about graphs so 
#i kept it. but the other one is cooler.

#the endign cutscene maybe?
#time to mess with the 3d renderer
#I'm actually going to do this? with manim?
from manim import *
from colour import *
from manim.opengl import *
#from manim.mobject.opengl.opengl_compatibility import ConvertToOpenGL

def trunOct(center, radius):
    vertTrun = [ # 0.01 for rendering "vertical" faces
        [ 2,  1,  0], #0
        [ 2, -1,  0], #1
        [-2,  1,  0], #2
        [-2, -1,  0], #3
        [ 0.01,  2.01,  1], #4
        [ 0,  2, -1], #5
        [ 0.01, -2.01,  1], #6
        [ 0, -2, -1], #7
        [ 1,  0,  2], #8
        [ 1,  0, -2], #9
        [-1,  0,  2], #10
        [-1,  0, -2], #11
        [ 1,  2,  0], #12
        [ 1, -2,  0], #13
        [-1,  2,  0], #14
        [-1, -2,  0], #15
        [ 0,  1,  2], #16
        [ 0,  1, -2], #17
        [ 0, -1,  2], #18
        [ 0, -1, -2], #19
        [ 2.01,  0.01,  1], #20
        [ 2,  0, -1], #21
        [-2.01,  0.01,  1], #22
        [-2,  0, -1], #23
    ]
    faceTrun = [
        [11, 17, 9, 19],
        [17, 9, 21, 0, 12, 5],
        [11, 17, 5, 14, 2, 23],
        [19, 11, 23, 3, 15, 7],
        [9, 19, 7, 13, 1, 21],
        #bottom half
        [5, 14, 4, 12],
        [21, 0, 20, 1],
        [7, 13, 6, 15],
        [23, 3, 22, 2],
        #top half
        [8, 16, 4, 12, 0, 20],
        [16, 10, 22, 2, 14, 4],
        [10, 18, 6, 15, 3, 22],
        [18, 8, 20, 1, 13, 6],
        [10, 16, 8, 18]
    ]

    for list in vertTrun:
        for i in range(len(list)):
            list[i] *= radius / 2
            list[i] += [center[0], center[1], center[2]][i]

    return Polyhedron(vertTrun, faceTrun)


class meeting(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        tunOc = trunOct([0,0,0], 1)

        def moveTrun(x, newcenter, radius):
            x1 = trunOct(newcenter, radius)
            self.remove(x.faces)
            self.add(x1.faces)
            return x1
        
        #15 fps for low
        #30 fps for medium
        #60 fps for high
        self.add(tunOc.faces)
        
        for t in range(60):
            self.wait(1 / 15)
            tunOc = moveTrun(tunOc, [0, 0, 3 * t / 60], 1)
        self.wait()
        
        #self.begin_ambient_camera_rotation(rate = 0.1)
        
        self.wait(30)
        
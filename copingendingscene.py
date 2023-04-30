# coping so hard rn
# my truncated octahedrons are simply not going to work
# so we use stupid spheres >:(
#
# slept. we not coping, we struggling
# bring me back the truncated octehedron
from manim import *
from colour import *
from manim.opengl import *

#py -m manim --renderer=opengl -pql .\copingendingscene.py ending --config_file manim1.cfg
#for green background use last statement

def makeSquare(u, v, type):
    x = u + v -1
    y = -u + v
    z = 2
    if type == 0:
        return [x, y, z]
    elif type == 1:
        return [x, y, -z]
    elif type == 2: 
        return [y, z, x]
    elif type == 3:
        return [y, -z, x]
    elif type == 4:
        return [z, y, x]
    elif type == 5:
        return [-z, y, x]
    else:
        return "bad >:("
def makeHexagon(u, v, type):
    x = 2 * u - 2
    y = v * (2 - np.abs(x + 1)) + np.max([0, x + 1])
    if type == 0:
        z = -1 * (3 + x - y)
    elif type == 1:
        y *= -1
        z = -1 * (3 + x + y)
    elif type == 2:
        x *= -1
        y *= -1
        z = -1 * (3 - x + y)
    elif type == 3:
        x *= -1
        z = -1 * (3 - x - y)
    elif type == 4:
        z = 1 * (3 + x - y)
    elif type == 5:
        y *= -1
        z = 1 * (3 + x + y)
    elif type == 6:
        x *= -1
        y *= -1
        z = 1 * (3 - x + y)
    elif type == 7:
        x *= -1
        z = 1 * (3 - x - y)
    else:
        z = "bad >:("
    return [x, y, z]
#my boy, he's here
# HES ALIVE 
def makeTrunOct(u, v):
    vector = []
    if u >= 13:
        u -= 13
        vector = makeSquare(u, v, 0)
    elif u >= 12:
        u -= 12
        vector = makeHexagon(u, v, 0)
    elif u >= 11:
        u -= 11
        vector = makeHexagon(u, v, 1)
    elif u >= 10:
        u -= 10
        vector = makeHexagon(u, v, 2)
    elif u >= 9:
        u -= 9
        vector = makeHexagon(u, v, 3)
    elif u >= 8:
        u -= 8
        vector = makeSquare(u, v, 1)
    elif u >= 7:
        u -= 7
        vector = makeSquare(u, v, 2)
    elif u >= 6:
        u -= 6
        vector = makeSquare(u, v, 3)
    elif u >= 5:
        u -= 5
        vector = makeSquare(u, v, 4)
    elif u >= 4:
        u -= 4
        vector = makeHexagon(u, v, 4)
    elif u >= 3:
        u -= 3
        vector = makeHexagon(u, v, 5)
    elif u >= 2:
        u -= 2
        vector = makeHexagon(u, v, 6)
    elif u >= 1:
        u -= 1
        vector = makeHexagon(u, v, 7)
    elif u >= 0:
        vector = makeSquare(u, v, 5)
    else:
        vector = "bad >:("
    return vector

class ending(ThreeDScene):
    def construct(self):
        sp = OpenGLSurface(makeTrunOct, [0, 14], [0, 1], color = BLUE, resolution = (101 * 14, 101))
        sph = OpenGLTexturedSurface(sp, "media/assets/purple.png", color = DARK_BLUE, resolution = (101 * 14, 101))
        sph1 = OpenGLTexturedSurface(sp, "media/assets/blue.png", color = DARK_BLUE, resolution = (101 * 14, 101))
        sph2 = OpenGLTexturedSurface(sp, "media/assets/red.png", color = DARK_BLUE, resolution = (101 * 14, 101))
        #ax = ThreeDAxes()

        self.set_camera_orientation(phi = 110 * DEGREES, theta = -30 * DEGREES)
        sph1.rotate(-9.5 * DEGREES, axis = OUT)
        sph2.rotate(9.5 * DEGREES, axis = OUT)

        sph.move_to([0, 35, -10]).scale(0.01)
        sph1.move_to([0 + 5, 35 + 1, -10]).scale(0.01)
        sph2.move_to([0 - 5, 35 + 1, -10]).scale(0.01)
        self.add(sph, sph1, sph2)
        self.wait()
        sph.generate_target()
        sph1.generate_target()
        sph2.generate_target()
        sph.target.scale(100)
        sph1.target.scale(100)
        sph2.target.scale(100)
        sph.target.move_to([0, 4, -1])
        sph1.target.move_to([5, 5, -1.5])
        sph2.target.move_to([-5, 5, -1.5])

        #light = self.camera.light_source
        #light.move_to([5, 10, 10])
        self.begin_ambient_camera_rotation(rate = 1.5 * DEGREES, about = 'theta')
        #20 seconds 75 degrees phi
        self.begin_ambient_camera_rotation(rate = 1.75 * DEGREES, about = 'phi')
        self.play(MoveToTarget(sph), MoveToTarget(sph1), MoveToTarget(sph2), run_time = 20)
        self.stop_ambient_camera_rotation(about = 'theta')
        self.stop_ambient_camera_rotation(about = 'phi')
        self.wait(2)
        self.move_camera(theta = -15 * DEGREES, phi = 110 * DEGREES, run_time = 5, frame_center = [6 * np.cos(15 * DEGREES), 0, 6 * np.cos(35 * DEGREES)])
        self.wait(4)
        self.move_camera(theta = 0, phi = 75 * DEGREES, frame_center = ORIGIN, run_time = 4)
        #self.move_camera(theta = 0, phi = 45 * DEGREES, run_time = 4)
        self.wait(3)
    

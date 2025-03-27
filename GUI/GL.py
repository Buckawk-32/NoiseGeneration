import OpenGL.GL
import OpenGL.GLU

import pygame

class Shader:

# For Cube Test
# --------------------------
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
        )

    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (5, 1),
        (5, 4),
        (5, 7),
        (6, 3),
        (6, 4),
        (6, 7)
        )
# --------------------------

    def __init__(self):
        pass


    def _test_buildCube(self):
        OpenGL.GL.glBegin(OpenGL.GL.GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                OpenGL.GL.glVertex3fv(self.vertices[vertex])

        OpenGL.GL.glEnd()

    def _test_runCube(self):
        window = Window(800, 600, "Shader - Cube Test")
        window.initialize()
        OpenGL.GLU.gluPerspective(45, (window.aspectRatio), 0.1, 50.0)

        OpenGL.GL.glTranslatef(0.0, 0.0, -5)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            OpenGL.GL.glRotatef(1, 3, 1, 1)
            OpenGL.GL.glClear(OpenGL.GL.GL_COLOR_BUFFER_BIT|OpenGL.GL.GL_DEPTH_BUFFER_BIT)
            self._test_buildCube()
            pygame.display.flip()
            window.wait(10)

class Window: 
    
    def __init__(self, width, height, title):
        self.x = width
        self.y = height
        self.title = title
        self.display = (width, height)
        self.aspectRatio = self.x/self.y


    def initialize(self):
        pygame.init()
        pygame.display.set_mode(self.display, pygame.DOUBLEBUF|pygame.OPENGL)
        pygame.display.set_caption(title=self.title)    


    def wait(self, time):
        pygame.time.wait(time)

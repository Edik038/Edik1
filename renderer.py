from itertools import starmap
from operator import mul
import pygame
from math import cos, sin, radians


class Mesh:

    def __init__(self, vertices, edges, polygons):

        self.vertices = vertices
        self.edges = edges
        self.polygons = polygons

    def clone(self):

        return Mesh(list(self.vertices), list(self.edges), list(self.polygons))


    def scale(self, x_factor, y_factor, z_factor):

        self.vertices = [[vertex[0] * x_factor, vertex[1] * y_factor, vertex[2] * z_factor]
                         for vertex in self.vertices]

    def rotate(self, x_angle, y_angle, z_angle):

        x_angle = radians(x_angle)
        y_angle = radians(y_angle)
        z_angle = radians(z_angle)

        matrix = [
            [cos(y_angle)*cos(z_angle), sin(x_angle)*sin(y_angle)*cos(z_angle)-cos(x_angle)
             * sin(z_angle), cos(x_angle)*sin(y_angle)*cos(z_angle)+sin(x_angle)*sin(z_angle)],
            [cos(y_angle)*sin(z_angle), sin(x_angle)*sin(y_angle)*sin(z_angle)+cos(x_angle)
             * cos(z_angle), cos(x_angle)*sin(y_angle)*sin(z_angle)-sin(x_angle)*cos(z_angle)],
            [-sin(y_angle), sin(x_angle)*cos(y_angle),
             cos(x_angle)*cos(y_angle)]
        ]

        self.vertices = [[sum(starmap(mul, zip(vertex, column))) for column in zip(*matrix)]
                         for vertex in self.vertices]

    def move(self, x_dist, y_dist, z_dist):

        self.vertices = [[vertex[0] + x_dist, vertex[1] + y_dist, vertex[2] + z_dist]
                         for vertex in self.vertices]


class Renderer:

    def __init__(self, window, clock, mesh, fill, perspective):

        self.window = window
        self.clock = clock
        self.running = True
        self.mesh = mesh
        self.fill = fill
        self.perspective = perspective

        self.background_color = (255, 255, 255)
        self.linecolor = (0, 0, 0)
        self.fillcolor = (0, 0, 0)
        self.background = pygame.Surface(self.window.get_size())
        self.delta_time = 0

    def draw(self):

        display_mesh = self.mesh.clone()
        display_mesh.rotate(10, 30, 0)
        display_mesh.scale(200, 200, 200)
        display_mesh.move(self.window.get_size()[0] / 2 - 100, self.window.get_size()[1] / 2 - 100, 0)
        display_vertices = [vertex[:-1] for vertex in display_mesh.vertices]

        if (self.fill):
            #pygame.draw.polygon(self.window, self.fillcolor, display_vertices)
            #pygame.draw.aalines(self.window, self.linecolor, True, display_vertices)
            pass
        else:
            for edge in display_mesh.edges:
                pygame.draw.aaline(self.window, self.linecolor, display_vertices[edge[0]], display_vertices[edge[1]])

    def run(self):

        while (self.running):
            self.background.fill(self.background_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.window.blit(self.background, (0, 0))
            self.draw()
            pygame.display.update()
            self.delta_time = self.clock.tick() / 1000


def main():

    pygame.init()

    WINDOW_SIZE = (800, 600)

    CUBE_VERTICES = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1]
    ]

    CUBE_EDGES = [
        [0, 1], [0, 2], [0, 3],
        [1, 4], [1, 5],
        [2, 4], [2, 6],
        [3, 5], [3, 6],
        [7, 4], [7, 5], [7, 6]
    ]

    renderer = Renderer(
        pygame.display.set_mode(WINDOW_SIZE, flags=pygame.SCALED, vsync=1),
        pygame.time.Clock(),
        Mesh(CUBE_VERTICES, CUBE_EDGES, []),
        False,
        False
    )
    renderer.run()

    pygame.quit()


main()

# Author: Maya Cole
# Date: 10/19/2021
# Purpose: create the Body class

from cs1lib import *

class Body:

    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    def update_position(self, timestep):
        self.x += self.vx * timestep
        self.y += self.vy * timestep

    def update_velocity(self, ax, ay, timestep):
        self.vx += ax * timestep
        self.vy += ay * timestep

    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        pixel_x = cx + self.x * pixels_per_meter
        pixel_y = cy - self.y * pixels_per_meter

        draw_circle(pixel_x, pixel_y, self.pixel_radius)

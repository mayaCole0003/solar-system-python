# Author: Maya Cole
# Date: 10/19/2021
# Purpose: create System class

import math
G = 6.67384 * 10 ** -11

class System:

    def __init__(self, body_list):
        self.body_list = body_list

    def compute_acceleration(self, curr_bod):
        ax = 0
        ay = 0
        for body in self.body_list:
            if body != curr_bod:
                dx = body.x - curr_bod.x
                dy = body.y - curr_bod.y
                r = math.sqrt(dx ** 2 + dy ** 2)
                a = (G * body.mass) / r ** 2
                temp_ax = a * (dx / r)
                temp_ay = a * (dy / r)
                ax += temp_ax
                ay += temp_ay

            return ax, ay

    def update(self, timestep):
        for body in self.body_list:
            body.update_position(timestep)
        for body in self.body_list:
            (ax, ay) = self.compute_acceleration(body)
            body.update_velocity(ax, ay, timestep)

    def draw(self, cx, cy, pixels_per_meter):
        for x in self.body_list:
            x.draw(cx, cy, pixels_per_meter)

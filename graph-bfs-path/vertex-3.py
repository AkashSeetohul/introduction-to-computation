#Copyright 2020 Tooryanand Seetohul

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

#  Lab assignment 3
#  Based on Professor Cormen's instructions
#  Author Tooryanand Seetohul

from cs1lib import *

RADIUS = 8

class Vertex:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adjacency_list = []

    #  method to add neighbors to the adjacency list
    def append_neighbor(self, other):
        self.adjacency_list.append(other)

    #  method to get list of adjacent neighbors
    def get_neighbors(self):
        return self.adjacency_list

    def __str__(self):

        adjacent_neighbors = ""  # empty string

        #  adding all the neighbors except the last
        for x in range(len(self.adjacency_list) - 1):
            adjacent_neighbors += str(self.adjacency_list[x]) + ", "

        #  adding the last neighbor without a space at the end
        adjacent_neighbors += self.adjacency_list[-1]

        return self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices: " + str(adjacent_neighbors)

    #  method to draw a vertex
    def draw_vertex(self, r, g, b):
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, RADIUS)

    #  method to draw the edges
    def draw_edge(self, other, r, g, b):
        set_stroke_color(r, g, b)

        #  draw the edges
        draw_line(self.x, self.y, other.x, other.y)
        draw_line(other.x, other.y, self.x, self.y)

    #  method to draw all adjacency edges
    def draw_adjacency_edges(self, r, g, b):
        set_stroke_color(r, g, b)

        #  looping through the adjacency list
        for z in self.adjacency_list:
            #  drawing the edges
            draw_line(self.x, self.y, z.x, z.y)
            draw_line(z.x, z.y, self.x, self.y)

    #  method to check if mouse is over object
    def is_mouse_over(self, x, y):
        return (self.x - RADIUS) <= x <= (self.x + RADIUS) and (self.y - RADIUS) <= y <= (self.y + RADIUS)

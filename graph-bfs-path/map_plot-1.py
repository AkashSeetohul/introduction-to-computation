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
from load_graph import *
from bfs import *
from vertex import Vertex


HEIGHT = 811
WIDTH = 1012

start_vertex = None
goal_vertex = None
mouse_press = False
mouse_move = False
vertices_dictionary = load_graph("dartmouth_graph.txt")


def press(mx, my):
    global mouse_press, mouse_x, mouse_y, start_vertex
    mouse_press = True
    mouse_x = mx
    mouse_y = my

    #  looping through the dictionary
    for key in vertices_dictionary:
        #  check if cursor is over the vertex
        if vertices_dictionary[key].is_mouse_over(mouse_x, mouse_y):
            start_vertex = vertices_dictionary[key]

def move(mx, my):
    global mouse_y, mouse_x, mouse_move, goal_vertex
    mouse_x = mx
    mouse_y = my
    mouse_move = True

    #  looping through the dictionary
    for key in vertices_dictionary:
        #  check if cursor is over the vertex
        if vertices_dictionary[key].is_mouse_over(mouse_x, mouse_y) and start_vertex:
            goal_vertex = vertices_dictionary[key]

def release(mx, my):
    global mouse_press, mouse_move
    mouse_press = False

img = load_image("dartmouth_map.png")

# vertices_dictionary = load_graph("dartmouth_graph.txt")

def main():
    global start_vertex, goal_vertex, mouse_press, mouse_move

    set_stroke_width(2)

    #  drawing the background
    draw_image(img, 0, 0)

    #  drawing all the vertices and adjacent edges
    for key in vertices_dictionary:
        vertices_dictionary[key].draw_vertex(0, 0, 1)
        vertices_dictionary[key].draw_adjacency_edges(0, 0, 1)

    #  check if start vertex and goal vertex do not hold 'None'
    if start_vertex and goal_vertex:

        #  find a path between them
        bfs_list = bfs(start_vertex, goal_vertex)

        #  draw the edges
        i = 1
        while i <= len(bfs_list) - 1:
            j = i - 1
            bfs_list[i].draw_edge(bfs_list[j], 1, 0, 0)
            i += 1


start_graphics(main, mouse_move=move, mouse_press=press, mouse_release=release, height=HEIGHT, width=WIDTH)

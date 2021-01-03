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

#  Lab assignment 2
#  Based on Professor Cormen's examples and instructions
#  Author Tooryanand Seetohul

from cs1lib import *

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 360

#  function to find x_coordinate of longitude
def find_x(the_list,index):
    return (float(the_list[index][3]) * 2) + 360

#  function to find x_coordinate of latitude
def find_y(the_list,index):
    return 360 - ((float(the_list[index][2]) * 2) + 180)

#  function to open file and create a list of references to world cities
def create_sorted_list(file_name, city_list):
    #  opening the text
    cities = open(file_name)

    #  looping through each line
    for line in cities:
        temporary_list = line.split(",") #  creating list with all four attributes
        #  appending the reference to the master city list
        city_list.append(temporary_list)

    #  closing the text
    cities.close()

sorted_cities = [] #  empty list to holde references to list of attributes
create_sorted_list("cities_population.txt", sorted_cities)

#  loading image file
img = load_image("world.png")

index = 0

def main():
    global index

    #  draw background image
    draw_image(img, 0, 0)

    set_fill_color(0, 0, 0) #  black

    #  drawing the cities
    x = 0
    while x <= index:
        draw_circle(find_x(sorted_cities, x), find_y(sorted_cities, x), 5)
        x += 1

    #  keep track of number of cities
    if index < 49:
        index += 1

start_graphics(main, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, framerate=1, title="The World")

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

#  Program to draw pong game
#  Author Tooryanand Seetohul
#  Based on Professor Cormen's examples and instructions

from cs1lib import *

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TOP_WALL_Y = 0
TOP_WALL_X = 0


PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
LEFT_PADDLE_X = 0
RIGHT_PADDLE_X = 380

PIXEL_MOVE = 7

pressed_a = False
pressed_z = False
pressed_k = False
pressed_m = False
pressed_q = False
pressed_space_bar = False

left_paddle_y = 0
right_paddle_y = 0

ball_center_x = 200
ball_center_y = 200

ball_speed_x = 3
ball_speed_y = 3

RADIUS = 10

initial_direction = True
bounce_to_the_left = False
bounce_to_the_right = False
bounce_to_the_top = False
bounce_to_the_bottom = False

def key_down(key):
    global pressed_a, pressed_k, pressed_m, pressed_z, pressed_q, pressed_space_bar
    if key == 'a':
        pressed_a = True
    elif key == 'z':
        pressed_z = True
    elif key == 'k':
        pressed_k = True
    elif key == 'm':
        pressed_m = True
    elif key == 'q':
        pressed_q = True
    elif key == ' ':
        pressed_space_bar = True

def key_up(key):
    global pressed_a, pressed_k, pressed_m, pressed_z, pressed_q, pressed_space_bar
    if key == 'a':
        pressed_a = False
    elif key == 'z':
        pressed_z = False
    elif key == 'k':
        pressed_k = False
    elif key == 'm':
        pressed_m = False
    elif key == 'q':
        pressed_q = False
    elif key == ' ':
        pressed_space_bar = False

def draw_ball():
    set_fill_color(0, 0, 0) #  black

    # removing outline of ball
    disable_stroke()

    draw_circle(ball_center_x, ball_center_y, RADIUS)


#  function to check for intersection with paddle or wall
def intersection_with_vertical(left_diameter_x, right_diameter_x, x_vertical_segment, ball_center_y, lower_segment_y, higher_segment_y):
    if (left_diameter_x <= x_vertical_segment <= right_diameter_x) and (higher_segment_y <= ball_center_y <= lower_segment_y):
        return True
    else:
        return False

#  function to check for intersection with top or bottom wall
def intersection_with_horizontal(top_diameter_y, bottom_diameter_y, y_horizontal_line):
    if top_diameter_y <= y_horizontal_line <= bottom_diameter_y:
        return True
    else:
        return False

#  function for the pong game
def main():
    global left_paddle_y, right_paddle_y, ball_center_x, ball_center_y, ball_speed_x, \
        initial_direction, bounce_to_the_left, bounce_to_the_right, bounce_to_the_top, bounce_to_the_bottom, ball_speed_y

    #  set background color yellow
    set_clear_color(1, 1, 0)
    clear()

    #  removing the outline
    disable_stroke()

    #  setting fill color yellow
    set_fill_color(0, 0, 1)

    #  draw left paddle
    draw_rectangle(LEFT_PADDLE_X, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    #  draw right paddle
    draw_rectangle(RIGHT_PADDLE_X, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

    #  if statements to control left paddle
    if left_paddle_y > 0 and pressed_a:
        left_paddle_y -= PIXEL_MOVE
    elif left_paddle_y < 320 and pressed_z:
        left_paddle_y += PIXEL_MOVE

    #  if statements to control right paddle
    if right_paddle_y > 0 and pressed_k:
        right_paddle_y -= PIXEL_MOVE
    elif right_paddle_y < 320 and pressed_m:
        right_paddle_y += PIXEL_MOVE

    #  if statement to end game if q is pressed
    if pressed_q:
        cs1_quit()

    #  if space bar to restart new game if necessary
    if pressed_space_bar:
        left_paddle_y = 0
        right_paddle_y = 0

        ball_center_x = 200
        ball_center_y = 200

        ball_speed_x = 3
        ball_speed_y = 3

        initial_direction = True
        bounce_to_the_left = False
        bounce_to_the_right = False
        bounce_to_the_top = False
        bounce_to_the_bottom = False

    draw_ball()

    if intersection_with_vertical(ball_center_x - RADIUS, ball_center_x + RADIUS, RIGHT_PADDLE_X, #  check for intersection with right paddle
                                  ball_center_y, right_paddle_y + PADDLE_HEIGHT, right_paddle_y):
        initial_direction = False
        bounce_to_the_left = True
        bounce_to_the_right = False
        bounce_to_the_top = False
        bounce_to_the_bottom = False

    if intersection_with_vertical(ball_center_x - RADIUS, ball_center_x + RADIUS, LEFT_PADDLE_X + PADDLE_WIDTH,
                                    ball_center_y, left_paddle_y + PADDLE_HEIGHT, left_paddle_y): #  check for intersection with left paddle
        initial_direction = False
        bounce_to_the_left = False
        bounce_to_the_right = True
        bounce_to_the_top = False
        bounce_to_the_bottom = False

    if intersection_with_vertical(ball_center_x - RADIUS, ball_center_x + RADIUS, 400, #  check for intersection with right wall
                                    ball_center_y, 400, 0):
        initial_direction = False
        bounce_to_the_left = False
        bounce_to_the_right = False
        bounce_to_the_top = False
        bounce_to_the_bottom = False

    if intersection_with_vertical(ball_center_x - RADIUS, ball_center_x + RADIUS, 0, #  check for intersection with left wall
                                    ball_center_y, 400, 0):
        initial_direction = False
        bounce_to_the_left = False
        bounce_to_the_right = False
        bounce_to_the_top = False
        bounce_to_the_bottom = False

    if intersection_with_horizontal(ball_center_y - RADIUS, ball_center_y + RADIUS, 0): # check for intersection with top of window
        initial_direction = False
        bounce_to_the_left = False
        bounce_to_the_right = False
        bounce_to_the_top = False
        bounce_to_the_bottom = True

    if intersection_with_horizontal(ball_center_y - RADIUS, ball_center_y + RADIUS, 400): # check for intersection with bottom of window
        initial_direction = False
        bounce_to_the_left = False
        bounce_to_the_right = False
        bounce_to_the_top = True
        bounce_to_the_bottom = False

    #  if statements to determine direction of ball
    if initial_direction:
        ball_center_y += ball_speed_y
        ball_center_x += ball_speed_x

    elif bounce_to_the_bottom:
        ball_speed_y = +3

        ball_center_y += ball_speed_y
        ball_center_x += ball_speed_y

    elif bounce_to_the_top:
        ball_speed_y = -3

        ball_center_y += ball_speed_y
        ball_center_x += ball_speed_x

    elif bounce_to_the_right:
        ball_speed_x = 3

        ball_center_y += ball_speed_y
        ball_center_x += ball_speed_x

    elif bounce_to_the_left:
        ball_speed_x = -3

        ball_center_y += ball_speed_y
        ball_center_x += ball_speed_x

start_graphics(main, title = "Pong", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, framerate = 50, key_press=key_down, key_release=key_up)



import pygame
import tkinter as tk
root = tk.Tk()

#constants
FPS = 60 # frames per second - try and do dynamically?
k_game_item_move_value = 3
k_initial_jump_velocity = 20
k_drop_acceleration = 1
k_gravity = .75
k_max_health = 100
k_max_zest = 100
k_ground_height = 20
k_wall_offset = 150
k_platform_offset = 400
k_time_between_game_items = .5
k_time_between_platforms = 2
k_time_between_boredom_drop = 4
k_boredom_drop_value = -5
k_out_of_box_time = 1.25
k_out_of_bounds = 50
k_game_item_offset = 75
k_bounce_dist = 150
k_sick_speed = 6
WIDTH_GW = 1020#root.winfo_screenwidth() # width of our game window
HEIGHT_GW = 620#root.winfo_screenheight() # height of our game window
BLACK = (0,0,0)
PLAYER_ACC = 4
PLAYER_FRICTION = -.5
BLACK = (0,0,0)
WHITE = (255, 255,255)
k_font_name = pygame.font.match_font('Comic Sans MS')

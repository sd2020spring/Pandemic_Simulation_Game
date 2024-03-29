#https://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
#https://kidscancode.org/blog/2016/08/pygame_1-2_working-with-sprites/
#https://kidscancode.org/blog/2016/08/pygame_1-3_more-about-sprites/

import pygame
import random
import os

WIDTH_GW = 360  # width of our game window
HEIGHT_GW = 480 # height of our game window
FPS = 30 # frames per second
BLACK = (0,0,0)
WHITE = (255, 255,255)

# initialize pygame and create window
pygame.init()
game_screen = pygame.display.set_mode((WIDTH_GW, HEIGHT_GW))
pygame.display.set_caption("COVID-19 Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


# set up asset folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'human.jpg')).convert()
tp_img = pygame.image.load(os.path.join(img_folder, 'tp.jpg')).convert()
sick_img = pygame.image.load(os.path.join(img_folder, 'sick.png')).convert()
egg_img = pygame.image.load(os.path.join(img_folder, 'egg.png')).convert()
mask_img = pygame.image.load(os.path.join(img_folder, 'mask.jpg')).convert()
guitar = pygame.image.load(os.path.join(img_folder, 'egg.png')).convert()
paint = pygame.image.load(os.path.join(img_folder, 'egg.png')).convert()
egg = pygame.image.load(os.path.join(img_folder, 'egg.png')).convert()
social = pygame.image.load(os.path.join(img_folder, 'egg.png')).convert()

#list of images of objects which decrease boredom
dec_bore_objs = [guitar, paint, egg, social]


class Player(pygame.sprite.Sprite): #sprite for player
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = player_img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH_GW / 2, HEIGHT_GW / 2)
		self.speedx = 0
		#self.speedy = 0

	def update(self, event):
		if event.type != KEYDOWN:
		    return
		if event.key == pygame.K_LEFT:#move left
		    player.speedx = -5
		if event.key == pygame.K_RIGHT: #move right
		    player.speedx = 5
		#if event.key == pygame.K_UP:
		    #player.speedy = 5 #move up
		#if event.key == pyfame.K_DOWN:
		    #player.speedy = -5 #move down


class TP(pygame.sprite.Sprite): #sprite for toilet paper
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = tp_img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH_GW - self.rect.width) #TP will randomly appear in the GW frame
		self.rect.y = random.randrange(0, 50) #TP will stay near ground since we are working on non platformer version
		self.speedx = random.randrange(-5, 5) #TP will move around screen

	def update(self): #if this is randomly selected for all objects, we can prob form this func outside and call in each class
		self.rect.x += self.speedx #speed in x direction gets randomized
		if self.rect.top > HEIGHT_GW:
			self.rect.x = random.randrange(WIDTH_GW - self.rect.width)
			self.rect.y = random.randrange(0, 50)
			self.speedx = random.randrange(-5, 5)

class SickPerson(pygame.sprite.Sprite): #sprite for sick person
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = sick_img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH_GW - self.rect.width) #TP will randomly appear in the GW frame
		self.rect.y = random.randrange(0, 50) #TP will stay near ground since we are working on non platformer version
		self.speedx = random.randrange(-5, 5) #TP will move around screen

	def update(self): #same movement as TP for the time being
		self.rect.x += self.speedx #speed in x direction gets randomized
		if self.rect.top > HEIGHT_GW:
		    self.rect.x = random.randrange(WIDTH_GW - self.rect.width)
		    self.rect.y = random.randrange(0, 50)
		    self.speedx = random.randrange(-5, 5)

class Ventilator(pygame.sprite.Sprite): #sprite for ventilator
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = ventilator_img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH_GW / 2, HEIGHT_GW / 2) #this needs to be randomized

class Mask(pygame.sprite.Sprite): #sprite for mask
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = mask_img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH_GW / 2, HEIGHT_GW / 2) #this needs to be randomized

class DecreaseBoredom(pygame.sprite.Sprite): #common sprite for all objects which decrease boredom
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = random.choice(dec_bore_objs) #pick randomly from a list of images of objects
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center =(WIDTH_GW / 2, HEIGHT_GW / 2) #randomly place object on screen

#collisions
BoredomCollisison = pygame.sprite.spritecollide(player, DecreaseBoredom, False)
if BoredomCollisison:
    change_zest(self, delta = 5) # this function is in objects.py

SickCollision = pygame.sprite.spritecollide(player, SickPerson, False)
if SickCollision:
	corona_contracted(self, delta = 20) # this function is in objects.py

TPCollision =  pygame.sprite.spritecollide(player, TP, False)
if TPCollision:
	get_toilet_paper(self, num_tp) #this function is in objects.py

MaskCollision = pygame.sprite.spritecollide(player, Mask, False)
if MaskCollision:
	health_improvement(self, health, delta= 10) #this function is in objects.py

VentilatorCollision = pygame.sprite.spritecollide(player, Ventilator, False)
if VentilatorCollision:
	health_improvement(self, health, delta= 20) #this function is in objects.py
	
#display text on screen. This is a very general function which can be used to visualize scores and any other visuals
#code heavily taken from http://kidscancode.org/blog/2016/08/pygame_shmup_part_7/ 
font_name = pygame.font.match_font('Comic Sans MS')

def draw_text_on_screen(surf, text, size, xpos, ypos):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (xpos, ypos)
    surf.blit(text_surface, text_rect)

# Game Loop
running = True
while 1==0:
    # Process input (events)

    # Update
   # Update
    all_sprites.update() #group of all sprites are updated

    # keep loop running at the right speed
    clock.tick(FPS)

    # Draw / render

 	#all updated sprites drawn

    # after drawing everything, flip the display to make it visible to viewer
    pygame.display.flip()

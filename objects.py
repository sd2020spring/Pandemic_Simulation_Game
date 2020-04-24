"""Creates the player character class and objects class"""
from model import *
import pygame

class PlayerCharacter(pygame.sprite.Sprite):
    """
    The player character of a top-down turn-based game.

    Attributes:
        x: the x-location of the character
        y: the y-location of the character
        display_char: the character to display for this character
        health: how much health the character has left (out of 100)
        zest: how bored your character is (max 100)
        num_tp: number of toilet paper rolls your character has

    """
    def __init__(self, image, x=0, y=0, health=100, zest=100, num_tp=0):
        """
        Create a player character.
        """
        self.x = x
        self.y = y
        self.health = health
        self.zest = zest
        self.num_tp = num_tp
        self.jumping = False
        self.jump_start_time = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        """updates the player position based on modified x and y coordinates
        """
        self.rect = (self.x,self.y)


    def change_health(self, delta = 20):
        """
        Changes the health of the character

        @delta      signed integer that changes the health
        @max_health integer that represents the max health of character

        returns     True if the health change results in a value greater than zero False if the character is dead!

        Raises:
            ValueError: if delta isn't an integer #don't know how to raise errors
        """

        if self.health + delta <= 0:
            return False
        if self.health <= self.max_health and self.health > 0:
            self.health = self.health - delta
        return True

        # Raise ValueError if delta isn't integer
        pass

    def change_zest(self, delta = 5):
        """
        Changes the zest of the character

        @delta    signed integer that changes the zest
        @max_zest integer that represents the max zest health of character

        returns   True if the zest change results in a value less than max_zest False if the character reaches max zest and dies!

        Raises:
            ValueError: if delta isn't an integer         #don't know how to raise errors
        """
        if self.zest >= self.max_zest:
            return false
        if self.zest > 0 and self.zest < self.max_zest:
            self.zest += delta
        return True

        # Raise ValueError if delta isn't integer
        pass

    def get_toilet_paper(self, num_tp):
        """
        Gets another roll of toilet paper.
        """
        # Increase character's toilet paper by one

        self.num_tp += 1
         #you would only call this function if your hits a toilet paper. in which case, would it not be easier to just add 1 instead of having this whole function?
        pass

class Object(pygame.sprite.Sprite):
    """
    The different objects that interact with the player.

    Attributes:
        delta_function: the function to call when a collision occurs, ex. player.get_toilet_paper,
        delta_value: the amount that the delta_function will change a value by
        image: the image that shows up when you display the object
        x: the x-location of the object
        y: the y-location of the object

    Examples of different objects:
        toilet paper: increases toilet paper by 1
        masks: increase health by 5
        activities: decrease zest by 5
        ventilator: increases health by 100
    """
    def __init__(self, delta_function, delta_value, image, x=320, y=270):
        """
        Create an object.
        """
        # Initialize variables
        self.delta_function = delta_function
        self.delta_value = delta_value
        self.type = type
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()


    def update(self):
        """updates the object position based on modified x and y coordinates
        """
        self.rect = (self.x,self.y)


    def contact_player(self):
        """
        Call the delta_function if the object collides with the player character

        Returns: None
        """
        #Call delta_function with delta_value as argument
        pass

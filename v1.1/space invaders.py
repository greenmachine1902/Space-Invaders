
__copyright__ = "(c) Matthew Johnson 2019"
__license__ = "Creative Commons Attribution-ShareAlike 2.0 Generic License."
__author__ = "Matt"
__version__ = "1.1"

#import required modules
import pygame as p #to simplify and shorten
import random #spawn asteroids in random positions
from modules.player import Player #class that handels all player functions


player = Player() #make the player class callable

p.init() #initiate pygame window and other elements

#sets the display width and height
width_display = 800
height_display = 600

#makes game display when called
gameDisplay = p.display.set_mode((width_display, height_display))

clock = p.time.Clock() #simplifies the clock module

p.display.set_caption("Space Invaders")#creates the title name for the window

#loads in the choosen image
spaceship = p.image.load("asserts/spaceship.png")
alien_one = p.image.load("asserts/aliens/alien 1.png")
alien_two = p.image.load("asserts/aliens/alien 2.png")

#scales the image to the required dimensions
ship_side = 60
spaceship = p.transform.scale(spaceship, (ship_side, ship_side))

#colours
dark_blue = (0, 50, 0)

#set the y position of the spaceship
spaceship_y = 500

#positions the spaceship initially in the middle of the screen
position = [(width_display/2)-(ship_side/2), spaceship_y]


#displays the background, player, asteroids and other updates
def display_update(spaceship, player_pos):    
    gameDisplay.fill(dark_blue) #fills background screen with colour
    gameDisplay.blit(spaceship, player_pos) #displays the spaceship at given coordinates
    gameDisplay.blit(alien_one, (0,0)) #displays the alien 1 at given coordinates
    gameDisplay.blit(alien_two, (0,50)) #displays the alien 2 at given coordinates

#handels quit game
def quit_game():
    p.quit() #quits pygame window
    quit() #quits python command exe

#main handels the intro, game, score and other functions
def main():
    game_exit = False #sets game_exit to false
    while not game_exit: #game loop
        for event in p.event.get(): #collects all events
            if event.type == p.QUIT: #checks events if quit button has been pressed
                quit_game() #goes to def function to quit

        #resets horizontal and vertical speed
        spaceship_x = 0
        
        keys = p.key.get_pressed() #if any key pressed
        if keys[p.K_LEFT] or keys[p.K_a]: #if left is pressed
            spaceship_x = -1 #moves the ship in that direction
        if keys[p.K_RIGHT] or keys[p.K_d]: #if right is pressed
            spaceship_x = 1 #moves the ship in that direction

        #calls ship movement function and gives required arguments 
        player.ship_movement(position, spaceship_x)

        display_update(spaceship, position) #calls the display function
        
        clock.tick(60) #sets frame rate speed for game
        p.display.update() #updates display

#checks to see if main is main
if __name__ == "__main__":
    main() #calls the main function

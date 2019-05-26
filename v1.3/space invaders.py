
__copyright__ = "(c) Matthew Johnson 2019"
__license__ = "Creative Commons Attribution-ShareAlike 2.0 Generic License."
__author__ = "Matt"
__version__ = "1.3"

#import required modules
import pygame as p #to simplify and shorten
import random #spawn asteroids in random positions
from modules.player import Player #class that handels all player functions
from modules.button import Button #class that handels all button functions
from modules.message import Message #class that handels all message functions


player = Player() #make the player class callable

p.init() #initiate pygame window and all other elements

#sets the display width and height
width_display = 800
height_display = 600

gameDisplay = p.display.set_mode((width_display, height_display)) #makes game display when called upon

clock = p.time.Clock() #simplifies the clock module

p.display.set_caption("Space Invaders")#creates the title name for the window

#loads in the choosen image
space_background = p.image.load("asserts/space background.png")
spaceship = p.image.load("asserts/spaceship.png")
alien_one = p.image.load("asserts/aliens/alien 1.png")
alien_two = p.image.load("asserts/aliens/alien 2.png")
bullet_img = p.image.load("asserts/bullet.png")

#scales the image to the required dimensions
ship_side = 60
bullet_side = 15
spaceship = p.transform.scale(spaceship, (ship_side, ship_side))
bullet_img = p.transform.scale(bullet_img, (bullet_side, bullet_side))
space_background = p.transform.scale(space_background, (width_display, height_display))

#colours
grey = (150, 150, 150)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (250, 250, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (200, 0, 150)
dark_red = (200, 0, 0)
dark_green = (0, 200, 0)
dark_blue = (0, 0, 200)
dark_pink = (150, 0, 200)

gameDisplay.fill(dark_blue) #fills background screen with colour

#set the y position of the spaceship
spaceship_y = 500

#simplify position 0, 0
origin = (0, 0)

#positions the spaceship initially in the middle of the screen
position = [(width_display/2)-(ship_side/2), spaceship_y]

#creats a list for the bullets
bullets = []

#sets the delay count for bullets spam
delay_count = 0

#menu screen handels title, start, quit, and instructions 
def menu_screen():
    #list of all buttons for menu screen
    menu_buttons = [Button("Play", 140, 280, 150, 100, blue, 60),
                    Button("Quit", 460, 280, 150, 100, red, 60),
                    Button("Instructions", 180, 420, 400, 100, pink, 60)]

    #list of all buttons for menu screen
    menu_messages = [Message("Space Invaders", 310, 80, white, 100)]

    run = True #sets run = true
    while run: #while true
        gameDisplay.blit(space_background, origin) #displays the background at given coordinates

        for message in menu_messages: #gets each message in list
            message.draw(gameDisplay) #draws the message and sends the gameDisplay
        
        for btn in menu_buttons: #gets each button in list
            btn.draw(gameDisplay) #draws the button and sends the gameDisplay
        
        for event in p.event.get(): #collects all events
            if event.type == p.QUIT: #checks events if quit button has been pressed
                quit_game() #goes to def function to quit
            if event.type == p.MOUSEBUTTONDOWN: #checks events if mouse has been pressed
                pos = p.mouse.get_pos() #gets the current mouse position
                for btn in menu_buttons: #gets each button in list
                    if btn.click(pos): #sends the mouse position to check if button has been clicked
                        if btn.text == "Play": #if button text = play
                            main() #calls main function
                        elif btn.text == "Quit": # if button text = quit
                            quit_game() #goes to def function to quit
                        elif btn.text == "Instructions": #if button text = instructions
                            instructions() #calls instructions function

        clock.tick(60) #sets frame rate speed for game
        p.display.update() #updates display

#instructions handels the title, controls and back button
def instructions():
    #loads in the required images
    left_click = p.image.load("asserts/instructions/left click.png")
    space = p.image.load("asserts/instructions/space.png")
    uldr = p.image.load("asserts/instructions/uldr.png")
    wasd = p.image.load("asserts/instructions/wasd.png")

    #sets the back button and title up
    back = Button("Back", 300, 420, 150, 100, red, 60)
    title = Message("Instructions", 300, 40, black, 100)
    
    run = True #sets run = true
    while run: #while true
        gameDisplay.fill(white) #fills the display with the color white
        
        for event in p.event.get(): #collects all events
            if event.type == p.QUIT: #checks events if quit button has been pressed
                quit_game() #goes to def function to quit
            if event.type == p.MOUSEBUTTONDOWN: #checks events if mouse has been pressed
                pos = p.mouse.get_pos() #gets the current mouse position
                if back.click(pos): #sends the mouse position to check if button has been clicked
                    if back.text == "Back": #if button text = back
                        menu_screen() #returns the player to the menu_screen

        #draws the button and title
        back.draw(gameDisplay)
        title.draw(gameDisplay)

        #displays the image at that position
        gameDisplay.blit(left_click, (100, 150))
        gameDisplay.blit(space, (400, 150))
        gameDisplay.blit(uldr, (60, 375))
        gameDisplay.blit(wasd, (490, 375))        
        
        clock.tick(60) #sets frame rate speed for game
        p.display.update() #updates display

#displays the background, player, asteroids and other updates
def display_update(player_pos, bullets):
    #displays the image at that position
    gameDisplay.blit(space_background, origin)
    gameDisplay.blit(spaceship, player_pos)
    gameDisplay.blit(alien_one, origin)
    gameDisplay.blit(alien_two, (0,50))
    
    for bullet in bullets: #for every bullet in bullets list
        #displays the bullet at given coordinates at index level      
        gameDisplay.blit(bullet_img, (bullet[0], bullet[1]))

#handels quit game
def quit_game():
    p.quit() #quits pygame window
    quit() #quits python command exe

#main handels the intro, game, score and other functions
def main():
    global delay_count #globals the delay_count to the main function can edit the count
    
    true = True #sets run to true
    while true: #game loop
        for event in p.event.get(): #collects all events
            if event.type == p.QUIT: #checks events if quit button has been pressed
                quit_game() #goes to def function to quit

        spaceship_x = 0 #resets horizontal speed
        
        keys = p.key.get_pressed() #if any key pressed
        if keys[p.K_LEFT] or keys[p.K_a]: #if left is pressed
            spaceship_x = -1 #moves the ship in that direction
        if keys[p.K_RIGHT] or keys[p.K_d]: #if right is pressed
            spaceship_x = 1 #moves the ship in that direction

        #calls ship movement function and gives required arguments 
        player.ship_movement(position, spaceship_x)

        delay_count += 1 #increases the delay count by 1

        #if delay count reaches 25 the following will run
        if delay_count >= 25:
            #collects the mouse state whether a button is being pressed
            mouse = p.mouse.get_pressed()

            #if left mouse or space is pressed
            if mouse[0] or keys[p.K_SPACE]:
                delay_count = 0 #resets the delay_count to 0
                #calls the create bullet function
                player.create_bullet(position, ship_side, bullet_side, bullets)

        player.update_bullet(bullets) #calls the update bullet function

        display_update(position, bullets) #calls the display function
        
        clock.tick(60) #sets frame rate speed for game
        p.display.update() #updates display

#checks to see if main is main
if __name__ == "__main__":
    menu_screen() #calls the main function

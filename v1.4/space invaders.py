
__copyright__ = "(c) Matthew Johnson 2019"
__license__ = "Creative Commons Attribution-ShareAlike 2.0 Generic License."
__author__ = "Matt"
__version__ = "1.4"

#import required modules
import pygame as p #to simplify and shorten
import random #spawn asteroids in random positions
from modules.player import Player #class that handels all player functions
from modules.enemy import Enemy #class that handels all enemy functions
from modules.button import Button #class that handels all button functions
from modules.message import Message #class that handels all message functions


player = Player() #make the player class callable
enemy = Enemy() #make the enemy class callable

p.init() #initiate pygame window and all other elements

#sets the display width and height
width_display = 800
height_display = 600

gameDisplay = p.display.set_mode((width_display, height_display)) #makes game display when called upon
p.display.set_caption("Space Invaders")#creates the title name for the window

clock = p.time.Clock() #simplifies the clock module

space_background = p.image.load("asserts/space background.png") #loads in the choosen image to be displayed later
#scales the image to the required dimensions
space_background = p.transform.scale(space_background, (width_display, height_display))

#library of colours
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

 
def menu_screen():
    """
    menu screen handels title, start, quit, and instructions
    :return:
    """
    #list of all buttons for menu screen
    menu_buttons = [Button("Play", 140, 280, 150, 100, blue, 60),
                    Button("Quit", 460, 280, 150, 100, red, 60),
                    Button("Instructions", 180, 420, 400, 100, pink, 60)]

    #list of all buttons for menu screen
    menu_messages = [Message("Space Invaders", (width_display/2), (height_display * (1/4)), white, 100)]

    run = True #sets run = true
    while run: #while true
        gameDisplay.blit(space_background, (0, 0)) #displays the background at given coordinates

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


def instructions():
    """
    instructions handels the title, controls and back button
    :return:
    """
    #loads in the required images
    left_click = p.image.load("asserts/instructions/left click.png")
    space = p.image.load("asserts/instructions/space.png")
    uldr = p.image.load("asserts/instructions/uldr.png")
    wasd = p.image.load("asserts/instructions/wasd.png")

    #sets up the back button and title up
    back = Button("Back", 300, 420, 150, 100, red, 60)
    title = Message("Instructions", 400, 60, black, 100)
    
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


def display_update(spaceship, bullet_img, player_pos, bullets, aliens, kill_count):
    """
    displays the background, player, asteroids and other updates
    :param spaceship: Img of spaceship
    :param player_pos: Int of player position
    :param bullets: List of bullets
    :param aliens: List of aliens
    :param kill_count: Int of kill count
    :return:
    """
    #displays the image at that position
    gameDisplay.blit(space_background, (0, 0))
    gameDisplay.blit(spaceship, player_pos)
    
    for bullet in bullets: #for every bullet in bullets list
        x = bullet[0] #seperates the x
        y = bullet[1] #seperates the y
        gameDisplay.blit(bullet_img, (x, y)) #displays the image at that position

    for alien in aliens: #for every alien in aliens list
            img = alien[0] #seperates the img from list
            pos = alien[1] #seperates the pos from list
            x = pos[0] #seperates the x from pos
            y = pos[1] #seperates the y from pos
            gameDisplay.blit(img, (x, y)) #displays the image at that position
            
    #list of all messages for menu screen
    score_message = [Message("Score:", 650, 40, white, 40), Message(kill_count, 750, 40, white, 40)]
    for message in score_message: #gets each message in list
        message.draw(gameDisplay) #draws the message and sends the gameDisplay


def quit_game():
    """
    handels quit game by closing pygame window and python window
    :return:
    """
    p.quit() #quits pygame window
    quit() #quits python command exe


def main():
    """
    main handels the main game and other functions
    :return:
    """
    #loads in the choosen images to be displayed later
    spaceship = p.image.load("asserts/spaceship.png")
    bullet_img = p.image.load("asserts/bullet.png")
    alien_one = p.image.load("asserts/aliens/alien 1.png")
    alien_two = p.image.load("asserts/aliens/alien 2.png")
    alien_three = p.image.load("asserts/aliens/alien 3.png")

    #sets the height and width of the object
    ship_side = 50
    alien_side = 35
    bullet_side = 15
    
    #scales the image to the required dimensions
    spaceship = p.transform.scale(spaceship, (ship_side, ship_side))
    bullet_img = p.transform.scale(bullet_img, (bullet_side, bullet_side))
    alien_one = p.transform.scale(alien_one, (alien_side, alien_side))
    alien_two = p.transform.scale(alien_two, (alien_side, alien_side))
    alien_three = p.transform.scale(alien_three, (alien_side, alien_side))

    spaceship_y = 500 #set the y position of the spaceship to be a constant
    position = [(width_display/2)-(ship_side/2), spaceship_y] #positions the spaceship initially in the middle of the screen

    #list of aliens that are available
    alien_imgs = [alien_one, alien_two, alien_three]

    #sets a delay to stop spam
    shooting_delay = 0
    alien_delay = 0

    kill_count = 0 #sets the score to zero

    #creats a list for the bullets and aliens
    bullets = []
    aliens = []
    
    true = True #sets run to true
    while true: #game loop
        for event in p.event.get(): #collects all events
            if event.type == p.QUIT: #checks events if quit button has been pressed
                quit_game() #goes to def function to quit

        direction = 0 #resets horizontal speed
        
        keys = p.key.get_pressed() #if any key pressed
        if keys[p.K_LEFT] or keys[p.K_a]: #if left is pressed
            direction = -1 #moves the ship in that direction
        if keys[p.K_RIGHT] or keys[p.K_d]: #if right is pressed
            direction = 1 #moves the ship in that direction

        #calls ship movement function and gives required arguments 
        player.ship_movement(position, direction, ship_side)

        #increases the delay count by 1
        shooting_delay += 1
        alien_delay += 1

        if shooting_delay >= 25: #if delay count reaches 25 the following will run
            #collects the mouse state whether a button is being pressed
            mouse = p.mouse.get_pressed()

            if mouse[0] or keys[p.K_SPACE]: #if left mouse or space is pressed
                shooting_delay = 0 #resets the shooting delay to 0
                #calls the create bullet function
                player.create_bullet(position, ship_side, bullet_side, bullets)

        player.update_bullet(bullets) #calls the update bullet function

        if alien_delay >= 60: #if delay count reaches 60 the following will run
            aliens = enemy.alien_spawn(aliens, alien_imgs) #calls the alien spawn function and returns the new list of aliens
            alien_delay = 0 #resets the alien delay to 0

        aliens = enemy.alien_movement(aliens) #updates the alien position and returns the new aliens list

        bullets, aliens, kill_count = enemy.check_hit(bullets, aliens, kill_count, alien_imgs) #checks if bullet hits an alien
        
        display_update(spaceship, bullet_img, position, bullets, aliens, kill_count) #calls the display function
        
        clock.tick(40) #sets frame rate speed for game
        p.display.update() #updates display

#checks to see if main is main
if __name__ == "__main__":
    menu_screen() #calls the main function

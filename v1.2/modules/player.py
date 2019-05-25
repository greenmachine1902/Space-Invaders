import pygame as p #to simplify and shorten
import math #import math module

#player class handels movement, shooting and other functions
class Player:
    def __init__(self):
        self.player_speed = 3 #sets the speed of which the ship can move
        self.ship_side = 60 #sets the side of the ship

    #checks if player can move then moves the player by changing its position
    def ship_movement(self, player_pos, spaceship_x):
        x_velocity = spaceship_x * self.player_speed #creates the x velocity

        #gets the current x and y position
        current_x = player_pos[0]

        #calculates the potential x and y
        potential_x = x_velocity + current_x

        #tests to see if potential position is within the width boundaries
        if (potential_x + self.ship_side) < 800 and potential_x > 0:
            #if true the current position will be updated with potential
            player_pos[0] = potential_x

    #creates the bullet at current ship x and y
    def create_bullet(self, position, ship_side, bullet_side, bullets):
        #calculates the x and y
        x = (position[0] + (ship_side / 2)) - (bullet_side / 2)
        y = position[1]

        #appends the position as a bullet
        bullets.append([x, y])

    #updates the bullets y position to animate it
    def update_bullet(self, bullets):
        #gets each bullet from bullets list
        for bullet in range(len(bullets)):
            #decreases the y position by 8 for that bullet
            bullets[bullet][1] -= 8

        #looks at all bullet's in bullets list
        for bullet in bullets[:]:
            #if bullet y reaches the top of screen
            if bullet[1] < 0:
                bullets.remove(bullet) #removes bullet from the bullets list
            
            
            

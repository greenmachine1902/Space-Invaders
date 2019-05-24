import pygame as p #to simplify and shorten

#player class handels movement, shooting and other functions
class Player:
    def __init__(self):
        self.speed = 3 #sets the speed of which the ship can move
        self.ship_side = 60 #sets the side of the ship

    #checks if player can move then moves the player by changing its position
    def ship_movement(self, player_pos, spaceship_x):
        x_velocity = spaceship_x * self.speed #creates the x velocity

        #gets the current x and y position
        current_x = player_pos[0]

        #calculates the potential x and y
        potential_x = x_velocity + current_x

        #tests to see if potential position is within the width boundaries
        if (potential_x + self.ship_side) < 800 and potential_x > 0:
            #if true the current position will be updated with potential
            player_pos[0] = potential_x
                

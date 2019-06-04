import pygame as p #to simplify and shorten

#player class handels movement, shooting and other functions
class Player:
    def __init__(self):
        self.player_speed = 3 #sets the speed of which the ship can move
        self.bullet_speed = 8 #sets the bullet speed to be a constant

    def ship_movement(self, player_pos, direction, ship_side):
        """
        checks if player can move then moves the player by changing its position
        :param player_pos: tuple The current position of where the player is located on the screen
        :param direction: int Direction of the players movement
        :param ship_side: int Size of the side of the ship
        :return:
        """
        x_velocity = direction * self.player_speed #creates the x velocity

        current_x = player_pos[0] #gets the current x and y position

        potential_x = x_velocity + current_x #calculates the potential x and y

        #tests to see if potential position is within the width boundaries
        if (potential_x + ship_side) < 800 and potential_x > 0:
            player_pos[0] = potential_x #if true the current position will be updated with potential

    def create_bullet(self, position, ship_side, bullet_side, bullets):
        """
        creates the bullet at current ship x and y
        :param position: tuple of player current position
        :param ship_side: int Size of the side of the ship
        :param bullet_side: int Size of the side of the bullet
        :param bullets: List of bullets that holds the position of each bullet
        :return:
        """
        x = (position[0] + (ship_side / 2)) - (bullet_side / 2) #calaculates the x
        y = position[1] #gets the y from player

        bullets.append([x, y]) #appends the position as a bullet

    def update_bullet(self, bullets):
        """
        updates the bullets y position to animate it
        :param bullets: List of bullets that holds the position of each bullet
        :return:
        """
        for bullet in range(len(bullets)): #gets each bullet from bullets list
            bullets[bullet][1] -= self.bullet_speed #changes the y position to animate the bullet

        for bullet in bullets[:]: #looks at all bullet's in bullets list
            y = bullet[1] #seperates the y from bullet
            if y < 0: #checks if bullet is greater than 0
                bullets.remove(bullet) #removes bullet from the bullets list

            
            
            

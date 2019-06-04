import pygame as p #to simplify and shorten
import random #imports random module from python

class Enemy:
    """
    player class handels movement, shooting and other functions
    """
    def __init__(self):
        self.alien_side = 35 #sets the side of the ship
        self.alien_speed = 0.25 #sets the alien movement speed
        self.bullet_side = 15 #sets the side of the bullet

    def alien_spawn(self, aliens, alien_imgs):
        """
        displays the background, player, asteroids and other updates
        :param spaceship: Img of spaceship
        :param player_pos: Int of player position
        :return List: aliens
        """
        x = random.randrange(20 + self.alien_side, 780 - self.alien_side) #randomizes the x pos for alien spawn
        y = -35 #sets the alien to spawn off the screen
        img = random.randrange(0, 3) #chooses a random number
        img = alien_imgs[img] #collects that img at that index level
        aliens.append([img, [x, y]]) #appends the new alien to aliens
        return aliens #returns the new aliens list

    def alien_movement(self, aliens):
        """
        checks if player can move then moves the player by changing its position
        :param aliens: list of all aliens
        :return List: aliens
        """
        for alien in range(len(aliens)): #gives each alien a number to use as index
            pos = aliens[alien][1] #seperates to pos from each alien
            y = pos[1] #seperates the y from pos
            y = y + self.alien_speed #updates the y pos to animate movement
            pos[1] = y #sets the pos y
            aliens[alien][1] = pos[1] #sets the new pos to the alien
        return aliens #returns the new aliens list

    def check_hit(self, bullets, aliens, kill_count, alien_imgs):
        """
        checks if any bullet hits any alien then removes both from lists
        :param bullets: List of bullets
        :param aliens: List of aliens
        :param kill_count: Int of score
        :param alien_imgs: List of alien imgs
        :return List: Bullets
        :return List: Aliens
        :return Int: Kill_count
        """
        for alien in aliens[:]: #looks at all alien in aliens list
            img = alien[0] #seperates the alien img from list
            pos = alien[1] #seperates the pos from list
            alien_x = pos[0] #seperates the x from pos
            alien_y = pos[1] #seperates the y from pos
            
            for bullet in bullets[:]: #looks at all bullet in bullets list
                bullet_x = bullet[0] #seperates the x from list
                bullet_y = bullet[1] #seperates the y from list

                #if bullet is within the alien hit box y
                if (bullet_y <= (alien_y + self.alien_side)) and (bullet_y >= alien_y):
                    #if bullet is within the alien hit box x
                    if (bullet_x >= (alien_x - self.bullet_side)) and (bullet_x <= (alien_x + self.alien_side)):
                        if img == alien_imgs[0]: #if current img is first in alien imgs
                            kill_count += 10 #plus amount of points assigned to the img
                        if img == alien_imgs[1]: #if current img is second in alien imgs
                            kill_count += 20 #plus amount of points assigned to the img
                        if img == alien_imgs[2]: #if current img is third in alien imgs
                            kill_count += 40 #plus amount of points assigned to the img
                        bullets.remove(bullet) #remove choosen bullet from bullets
                        aliens.remove(alien) #remove choosen alien from aliens
               
        return bullets, aliens, kill_count #returns these variables to where it was being called

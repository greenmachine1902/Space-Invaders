import pygame as p #to simplify and shorten

p.font.init() #initiate font elements

class Button:
    """
    handles making buttons like start, quit and other functions
    """
    def __init__(self, text, x, y, w, h, colour, size):
        self.text = text #sets text to equal text
        self.x = x #sets x to equal x
        self.y = y #sets y to equal y
        self.w = w #sets the width
        self.h = h #sets the height
        self.colour = colour #sets colour to equal colour
        self.size = size #sets size to equal size

    def draw(self, gameDisplay):
        """
        collects the text surface to draw text and rect
        :param gameDisplay: The game screen
        :return:
        """
        #draws a rect around the text with the choosen colour
        p.draw.rect(gameDisplay, self.colour, (self.x, self.y, self.w, self.h))
        text_font = p.font.SysFont("comicsansms", self.size) #gets the choosen font and size to render later
        text_surface = text_font.render(self.text, True, (255, 255, 255)) #renders the text with the choosen colour
        text_rect = text_surface.get_rect() #gets the rect from text surface
        text_rect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2))) #gets the center of the text
        gameDisplay.blit(text_surface, text_rect) #blits the text to the game display

    def click(self, pos):
        """
        gets the mouse and checks to see if it has been clicked within box
        :param pos: The position of the mouse
        :return: True or False
        """
        #seperates the x and y pos
        x_pos = pos[0]
        y_pos = pos[1]

        #if clicked within the boundries
        if self.x <= x_pos <= self.x + self.w and self.y <= y_pos <= self.y + self.h:
            return True #returns true that button was clicked
        else:
            return False #returns false that button was clicked

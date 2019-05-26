import pygame as p #to simplify and shorten

p.font.init() #initiate font elements

#sets the display width and height
width = 800
height = 600

#handles making messages like titles and other text objects
class Message:
    def __init__(self, text, x, y, colour, size):
        self.text = text #sets text to equal text
        self.x = x #sets x to equal x
        self.y = y #sets y to equal y
        self.width = 180 #sets the width
        self.height = 120 #sets the height
        self.colour = colour #sets colour to equal colour
        self.size = size #sets size to equal size

    #renders the text in that font and returns it to draw
    def text_objects(self, text, font, colour):
        #renders the text with the choosen colour
        text_surf = font.render(str(text), True, colour)
        #returns the text surface
        return text_surf, text_surf.get_rect()

    #collects the text surface to draw text
    def draw(self, gameDisplay):
        #gets the choosen font and size to render later
        text_font = p.font.SysFont("comicsansms", self.size)
        #gets the text surface
        text_surf, text_rect = self.text_objects(self.text, text_font, self.colour)
        #finds the center of the text
        text_rect.center = ((self.x + (self.width / 2)), (self.y + (self.height / 2)))
        #blits the text to the game display
        gameDisplay.blit(text_surf, text_rect)

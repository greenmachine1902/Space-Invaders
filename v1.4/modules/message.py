import pygame as p #to simplify and shorten

p.font.init() #initiate font elements

class Message:
    """
    handles making messages like titles and other text objects
    """
    def __init__(self, text, x, y, colour, size):
        self.text = text #sets text to equal text
        self.x = x #sets x to equal x
        self.y = y #sets y to equal y
        self.colour = colour #sets colour to equal colour
        self.size = size #sets size to equal size

    def draw(self, gameDisplay):
        """
        collects the text surface to draw text and rect
        :param gameDisplay: The game screen
        :return:
        """
        text_font = p.font.SysFont("comicsansms", self.size) #gets the choosen font and size to render later
        text_surface = text_font.render(str(self.text), True, self.colour) #renders the text with the choosen colour
        text_rect = text_surface.get_rect() #gets the rect from text surface
        text_rect.center = (self.x, self.y) #updates the center of the text
        gameDisplay.blit(text_surface, text_rect) #blits the text to the game display

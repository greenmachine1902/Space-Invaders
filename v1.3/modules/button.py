import pygame as p #to simplify and shorten

p.font.init() #initiate font elements

#sets the display width and height
width = 800
height = 600

#handles making buttons like start, quit and other functions
class Button:
    def __init__(self, text, x, y, w, h, colour, size):
        self.text = text #sets text to equal text
        self.x = x #sets x to equal x
        self.y = y #sets y to equal y
        self.w = w #sets the width
        self.h = h #sets the height
        self.colour = colour #sets colour to equal colour
        self.size = size #sets size to equal size

    #renders the text in that font and returns it to draw
    def text_objects(self, text, font, colour):
        #renders the text with the choosen colour
        text_surf = font.render(str(text), True, colour)
        #returns the text surface
        return text_surf, text_surf.get_rect()

    #collects the text surface to draw text and rect
    def draw(self, game_display):
        #draws a rect around the text with the choosen colour
        p.draw.rect(game_display, self.colour, (self.x, self.y, self.w, self.h))
        #gets the choosen font and size to render later
        text_font = p.font.SysFont("comicsansms", self.size)
        #gets the text surface
        text_surf, text_rect = self.text_objects(self.text, text_font, (255, 255, 255))
        #finds the center of the text
        text_rect.center = ((self.x + (self.w / 2)), (self.y + (self.h / 2)))
        #blits the text to the game display
        game_display.blit(text_surf, text_rect)

    #gets the mouse and checks to see if it has been clicked within box
    def click(self, pos):
        #seperates the x and y pos
        x_pos = pos[0]
        y_pos = pos[1]

        #if clicked within the boundries
        if self.x <= x_pos <= self.x + self.w and self.y <= y_pos <= self.y + self.h:
            return True #returns true that button was clicked
        else:
            return False #returns false that button was clicked

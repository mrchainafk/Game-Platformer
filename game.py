from tkinter import *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title('Junkman in repository')
        self.tk.resizable(0, 0)
        self.tk.wn_attributes('-topmost', 1)
        self.canvas = Canvas(self.tk, width = 500, height = 500, \
            highlightthickness = 0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_width = 500
        self.canvas_height = 500
        self.bg = PhotoImage(file = 'background.gif')
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0, 5):
            for y in range(0, 5):
                self.canvas.create_image(x * w, y * h, \
                    image = self.bg, anchor = 'nw')
        self.sprites = []
        self.running = True 

def mainloop(self):
    while 1:
        if self.running == True:
            for sprite in self.sprites:
                sprite.move()
        self.tk.update_idletasks()
        self.tk.update()
        time.sleep(0.01)

class Coords:
    def __init__(self, x1=0, x2=0, y1=0, y2=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

def within_x(co1, co2):
    if(co1.x1 > co2.x1 and co1.x1 < co2.x2) \
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
            or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
            or (co2.x2 > co1.x1 and co2.x2 < co1.x2) \
        return True
    else:
        return False

def within_y(co1, co2):
    if(co1.y1 > co2.y1 and co1.y1 < co2.y2) \
            or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
            or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
            or (co2.y2 > co1.y1 and co2.y2 < co1.y2) \
        return True
    else:
        return False

def collited_right(co2, co1):
    if within_y(co2, co1):
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
            return True
    return False

def collited_left(co2, co1):
    if within_y(co2, co1):
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
            return True
    return False

def collited_top(co2, co1):
    if within_x(co2, co1):
        if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
            return True
    return False

def collited_bottom(y, co1, co2):
    if within_x(co1, co2):
        y_calc = co1.y2 + y
        if y_calc >= co2.y1 and y_calc <= co2.y2:
            return True
    return False

class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None
    def move(self):
        pass
    def coords(self):
        return self.coordinates

class platformFigureSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, \
            image = self.photo_image, anchor = 'nw')
        self.coordinates = Coords(x, y, x + width, y + height)

class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game):
        self.images_left = [
            PhotoImage(file=''),
            PhotoImage(file=''),
            PhotoImage(file='')
        ]
        self.images_right = [
            PhotoImage(file=''),
            PhotoImage(file=''),
            PhotoImage(file='')
        ]
        self.image = game.canvas.create_image(200, 470, \
                image = self.images_left[0], anchor = 'nw')
        
        self.x = -2
        self.y = 0
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = Coords()
        
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)

    def turn_left(self, evt):
        if self.y == 0:
            self.x = -2
    
    def turn_right(self, evt):
        if self.y == 0:
            self.x = 2

    def jump(self, evt):
        if self.y == 0:
            self.y == -4
            self.jump_count = 0

    def aselnimate(f):
        if self.x != 0 and self.y != 0:
            if time.time() - self.last_time > 0.1:
                self.last_time = time.time()
                self.current_image += self.current_image_add
                if self.current_image >= 2:
                    self.current_image_add = -1
                if self.current_image <= 0:
                    self.current_image_add = 1
        if self.x < 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, \
                    image = self.images_left[2])
            else:
                self.game.canvas.itemconfig(self.image, \
                    image = self.images_left[ \
                        self.current_image]) 
            elif self.x > 0:
                if self.y != 0:
                    self.game.canvas.itemconfig(self.image, \
                        image = self.images_right[2])
                else:
                    self.game.canvas.itemconfig(self.image, \
                        image = self.images_right[
                            self.current_image])

    

        


    




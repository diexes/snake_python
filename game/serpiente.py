import pygame
from pygame import Surface
class Cuerpo:
    __block = None
    def __init__(self,superficie:Surface, pos:tuple):
        if Cuerpo.__block == None:
            Cuerpo.__block = pygame.image.load("resources/block.jpg").convert()
        self.superficie = superficie
        self.__x = pos[0]
        self.__y = pos[0]

    def draw(self):
        self.superficie.blit(self.__block, (self.__x, self.__y))

    def set_pos(self,pos:tuple):
        self.__x = pos[0]
        self.__y = pos[1]

    def get_pos(self):
        x = self.__x
        y = self.__y
        return (x, y)

class Serpiente:
    __DIMENSION = 40

    def __init__(self, superficie:Surface, length):
        self.__length = length
        self.__cuerpo = []
        for i in range(length):
            self.__cuerpo.append(Cuerpo(superficie, (self.__DIMENSION,self.__DIMENSION)))
        self.__superficie = superficie
        self.direction = 'down'
        self.__block = pygame.image.load("resources/block.jpg").convert()

    def draw(self):
        for i in range(self.__length):
            self.__cuerpo[i].draw()

    def reset(self):
        for i in range(0, self.__length -1):
            p = self.__cuerpo.pop()
            self.__length -= 1


    def add__cola(self):
        pos_final = self.__cuerpo[-0].get_pos()
        print(pos_final)
        new_cola = Cuerpo(self.__superficie, pos_final)
        self.__length += 1
        self.__cuerpo.append(new_cola)

    def move(self):

        for i in range(self.__length - 1, 0, -1):
            block = self.__cuerpo[i-1].get_pos()
            self.__cuerpo[i].set_pos(block)

        pos = self.__cuerpo[0].get_pos()
        if(self.direction == 'up'):
            self.__cuerpo[0].set_pos((pos[0], pos[1] - self.__DIMENSION))
        elif(self.direction == 'down'):
            self.__cuerpo[0].set_pos((pos[0], pos[1] + self.__DIMENSION))
        elif(self.direction == 'left'):
            self.__cuerpo[0].set_pos((pos[0] - self.__DIMENSION, pos[1]))
        elif(self.direction == 'rigth'):
            self.__cuerpo[0].set_pos((pos[0] + self.__DIMENSION, pos[1]))
        self.draw()

    def get_pos(self):
        return self.__cuerpo[0].get_pos()

    def move_up(self):
        if(self.direction != 'down'):
            self.direction = 'up'

    def move_down(self):
        if (self.direction != 'up'):
            self.direction = 'down'

    def move_rigth(self):
        if (self.direction != 'left'):
            self.direction = 'rigth'

    def move_left(self):
        if (self.direction != 'rigth'):
            self.direction = 'left'

    def detect_colision(self):
        pos_snake = self.__cuerpo[0].get_pos()
        for i in range(1, self.__length):
            pos_cuerpo = self.__cuerpo[i].get_pos()
            if((pos_snake[1] +20 < pos_cuerpo[1] + 40 and pos_snake[1] +20 > pos_cuerpo[1]) and (pos_snake[0] +20 < pos_cuerpo[0] + 40 and pos_snake[0] +20 > pos_cuerpo[0])):
                return True
        return False
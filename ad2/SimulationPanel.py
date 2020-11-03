#!/usr/bin/env python
# coding: UTF-8
#
# @package SimulationPanel
# @author Ariadne Pinheiro
# @date 08/10/2020
#
# Class for presenting the simulation in a graphical form.
#
##

from random import randint
from Disease import Disease
from tkinter import Tk, Canvas
from MyWorld import MyWorld
from Timer import Timer
from mapper import mapper
import sys


class SimulationPanel:
    # Constructor
    def __init__(self, world, canvas):
        self.__world = world
        self.__canvas = canvas
        self.__dict = dict()
        self.__widthScale = 1
        self.__heightScale = 1
        self.__wvmap = None

    # Return the distance between two circles
    def distance2circles(self, ab, bc):
        return ((ab[0] - bc[0]) ** 2 + (ab[1] - bc[1]) ** 2) ** 0.5

    # Create the border of the self.world as a rectangle
    def draw(self):
        objects = self.__world.getObjects()
        self.auxDraw()
        self.__world.act()
        for disease in objects:
            disease.act()

    # Draw all objects in it as circles
    def auxDraw(self):
        objs = self.__world.getObjects()
        self.__canvas.delete('all')

        # Quadrants
        self.__canvas.create_line((int(self.__canvas['width']) // 2) * self.__widthScale,
                                  0,
                                  (int(self.__canvas['width']) // 2) * self.__widthScale,
                                  (int(self.__canvas['height']) * self.__heightScale),
                                  width=2, fill='blue')
        self.__canvas.create_line(0,
                                  (int(self.__canvas['height']) // 2) * self.__heightScale,
                                  (int(self.__canvas['width']) * self.__widthScale),
                                  (int(self.__canvas['height']) // 2) * self.__heightScale,
                                  width=2, fill='blue')

        # Grid
        for value in range(self.__world.getWidth()):
            p = self.__wvmap.windowToViewport((value, 0))[0]
            self.__canvas.create_line(p[0] * self.__widthScale,
                                      0,
                                      p[0] * self.__widthScale,
                                      (int(self.__canvas['height']) * self.__heightScale),
                                      width=1, fill='white', dash=(2, 2))
        for value in range(self.__world.getHeight()):
            p = self.__wvmap.windowToViewport((0, value))[0]
            self.__canvas.create_line(0,
                                      p[1] * self.__heightScale,
                                      (int(self.__canvas['width']) * self.__widthScale),
                                      p[1] * self.__heightScale,
                                      width=1, fill='white', dash=(3, 2))

        # Diseases
        for disease in objs:
            p = self.__wvmap.windowToViewport((disease.getX(), disease.getY()))[0]
            self.__canvas.create_oval((p[0] - (disease.getStrength() % self.__dict[p])) * self.__widthScale,
                                      (p[1] - (disease.getStrength() % self.__dict[p])) * self.__heightScale,
                                      (p[0] + (disease.getStrength() % self.__dict[p])) * self.__widthScale,
                                      (p[1] + (disease.getStrength() % self.__dict[p])) * self.__heightScale,
                                      fill=self.rgb())

    # Resize Window
    def resize(self, event=None):
        self.auxDraw()
        self.__canvas.pack(fill="both", expand=1)
        self.__heightScale = float(event.height) / float(self.__canvas['height'])
        self.__widthScale = float(event.width) / float(self.__canvas['height'])

    # Callback for mouse button-1 pressed
    def mousePressed(self, event):
        try:
            p = self.__wvmap.viewportToWindow(event.x, event.y)

            if abs(int(p[0]) - p[0]) <= 0.5:
                x_cell = int(p[0])
            else:
                x_cell = int(p[0]) + 1

            if abs(int(p[1]) - p[1]) <= 0.5:
                y_cell = int(p[1])
            else:
                y_cell = int(p[1]) + 1

            obj = Disease()
            self.__world.addObject(obj, x_cell, y_cell)
            obj.setGrowthCondition(self.__world.getTemp(obj.getQuadrant()) - 1,
                                   self.__world.getTemp(obj.getQuadrant()) + 1,
                                   2.5)

            self.__animation()

        except SyntaxError:
            print("Número máximo de objetos nessa célula")
        else:
            print("Novos objetos foram adicionados")

    # Save simulation data onto a file
    def printData(self):
        objs = self.__world.getObjects()
        locals = ""
        growthConditions = ""

        for obj in objs:
            locals = locals + str(obj.getX()) + ',' + str(obj.getY()) + ';'
            dt = obj.getGrowthCondition()
            growthConditions = growthConditions + str(dt[1]) + ',' + str(dt[2]) + ',' + str(dt[0]) + ';'

        string = f'NumDiseases={len(objs)}\n' \
                 f'Locations={locals.rstrip(";")}\n' \
                 f'DiseasesGrowth={growthConditions.rstrip(";")}\n' \
                 f'Temperature={str(self.__world.getTemp(0))};{str(self.__world.getTemp(1))};' \
                 f'{str(self.__world.getTemp(2))};{str(self.__world.getTemp(3))}'

        with open('simulation-results.config', 'rw') as arq:
            arq.write(string)

    # Toggle animation
    def __animation(self):
        objects = self.__world.getObjects()

        for disease in objects:
            p = self.__wvmap.windowToViewport((disease.getX(), disease.getY()))[0]
            self.__dict[p] = 0

        points = list(self.__dict.keys())
        for p1 in points:
            for p2 in points:
                radius = self.distance2circles(p1, p2) // 2

                if radius < self.__dict[p1] or (self.__dict[p1] == 0 and radius != 0):
                    if radius != 0:
                        self.__dict[p1] = radius

                if radius < self.__dict[p2] or (self.__dict[p2] == 0 and radius != 0):
                    if radius != 0:
                        self.__dict[p2] = radius

    def rgb(self):
        red = str(hex(randint(0, 255))).lstrip('0x').rjust(2, '0')
        green = str(hex(randint(0, 255))).lstrip('0x').rjust(2, '0')
        blue = str(hex(randint(0, 255))).lstrip('0x').rjust(2, '0')
        return "#" + red + green + blue

    @property
    def wvmap(self):
        return self.__wvmap

    @wvmap.setter
    def wvmap(self, q):
        self.__wvmap = q
        self.__animation()


def main():
    wsizex = 512
    wsizey = 512
    margin = 10
    root = Tk()
    root.title("Simulador de Doenças")
    world = MyWorld()

    # maps the world rectangle onto a viewport of wsizex x wsizey pixels.
    canvas = Canvas(root, width=wsizex, height=wsizey, background='dark grey')
    canvas.pack()
    sp = SimulationPanel(world, canvas)
    sp.wvmap = mapper([0, 0, world.getWidth() - 1, world.getHeight() - 1],
                      [margin, margin, wsizex - margin, wsizey - margin], False, False)

    poll = Timer(root, sp.draw, 500)
    canvas.bind('<Configure>', sp.resize)
    root.bind('<Escape>', lambda _: root.destroy())
    root.bind('s', lambda _: poll.stop())
    root.bind('r', lambda _: poll.restart())
    root.bind('p', sp.printData)
    root.bind('<Button -1 >', lambda e: sp.mousePressed(e))
    poll.run()
    root.mainloop()


if __name__ == '__main__':
    sys.exit(main())

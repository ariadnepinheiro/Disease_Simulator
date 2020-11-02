# !/usr/bin/env python
# coding: UTF-8
#
# @package Simulator
# @author Ariadne Pinheiro
# @date 08/10/2020
#
# Simulator class, to simulate in a GUI, one fictional world of diseases.
#
##

from tkinter import Tk, Canvas
from MyWorld import MyWorld
from SimulationPanel import SimulationPanel
from Timer import Timer
from mapper import mapper
import sys


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

#!/usr/bin/env python
# coding: UTF-8
#
## @package Simulator

from Actor import Actor
from MyWorld import MyWorld
from World import World
import sys
import getopt


##
# Simulator class, to simulate the growth of diseases in a fictional world.
#
# Resolução da AD1 2020.2 - Prog. de Interfaces Gráficas - TSC/UFF
# @author ARIADNE GONÇALVES PINHEIRO
# Matrícula: 19113050151
# Pólo: Duque de Caxias
# @date 26/08/2020
#
##
# This is the main method that
# sets up a virtual world and simulates the growth of
# the diseases in the world .
# If the number of iterations is given in the command line
# argument , run the simulation for that many number
# of iterations .
# Otherwise , use the default number of iterations : 5.
#

def main(args=None):

    options, myArgs = getopt.getopt(sys.argv[1:], "n:")

    if options == []:
        numItr = 5
    else:
        filled = int(options[0][1])
        numItr = filled

    print("Simulation of My World")
    myworld = MyWorld()

    for i in range(numItr):
        myworld.act()
        objects = myworld.getObjects()
        for j in objects:
            j.act()
    print("")

    print("Simulation of World")
    world = World(100, 100)

    actor1 = Actor()
    actor2 = Actor()

    world.addObject(actor1, 10, 10)
    world.addObject(actor2, 90, 90)

    for i in range(numItr):
        world.act()
        objects = world.getObjects()
        for j in objects:
            j.act()


if __name__ == '__main__':
    sys.exit(main())

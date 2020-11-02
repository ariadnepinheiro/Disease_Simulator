#!/usr/bin/env python
# coding: UTF-8
#
## @package WorldTest

from Actor import Actor
from World import World
import unittest
import random


##
#
# WorldTest class
#
# Resolução da AD1 2020.2 - Prog. de Interfaces Gráficas - TSC/UFF
# @author ARIADNE GONÇALVES PINHEIRO
# Matrícula: 19113050151
# Pólo: Duque de Caxias
# @date 26/08/2020
#

class WorldTest(unittest.TestCase):
    ##
    # Test the initialization of the constructor that it is placed appropriately
    #
    def TestConstructorAndGetMethods(self):
        world = World(5, 10)

        self.assertEqual(10, world.getHeight())
        self.assertEqual(5, world.getWidth())
        self.assertEqual(0, world.numberOfObjects())

    ##
    # Test that the objects that are placed are still the objects when retrieved
    #
    def testGetObjects(self):
        world = World(5, 5)
        rand = int(random.randint(0, 10))

        # Ready 5 actors to be placed
        actors = []

        for i in range(0, 5):
            actors.append(Actor())

        objH = random.randint(0, world.getHeight() - 1)
        objW = random.randint(0, world.getWidth() - 1)

        # Randomly place 5 objects into the world
        for i in range(5):
            world.addObject(actors[i], objH, objW)

        # There should only be 5 actors in total
        self.assertEqual(5, world.numberOfObjects())

        # The actors should be retrieved
        objects = world.getObjects()

        self.assertEqual(len(actors), len(objects))

        for i in range(0, len(objects)):
            matchFound = False

            for j in range(0, len(objects)):
                if (objects[i] == objects[j]):
                    matchFound = True
                    break

    ##
    # Test that the number of object function returns the correct result
    #
    def testNumberOfObject(self):
        world = World(5, 5)

        objH = random.randint(0, world.getHeight() - 1)
        objW = random.randint(0, world.getWidth() - 1)

        # Randomly place 5 objects into the world
        for i in range(5):
            world.addObject(Actor(), objH, objW)

        # There should only be 5 actors in total
        self.assertEqual(5, world.numberOfObjects())

    ##
    # Test if the copying of grid
    # @throws Exception if the aGrid consists of invalid properties
    #
    def testSetGrid(self):
        with self.assertRaises(Exception):
            world = World(5, 5)
            aGrid = Actor[None][None][5]

            # Randomly create a grid into the aGrid
            x = int(random.randint(0, 3))
            y = int(random.randint(0, 3))

            for i in range(5):
                if world.aGrid[x][y][i] is None:
                    world.aGrid[x][y][i] = Actor()
                    break

            # Copy the aGrid to the world
            with self.assertRaises(Exception):
                world.setGrid(aGrid)

            # Match and compare
            self.assertEqual(3, world.getWidth())
            self.assertEqual(3, world.getHeight())
            self.assertEqual(5, world.numberOfObjects())

    ##
    # Test that the add object function captures this error
    # @throws SyntaxError when already max number of objects are in that cell
    # expected = SyntaxError.class
    #
    def testAddObjectSyntaxError(self):
        world = World(1, 1)

        # Fill the world with 5 actors
        for i in range(5):
            world.addObject(Actor(), 0, 0)

        # Fill it with the sixth actor which will throw the exception
        with self.assertRaises(SyntaxError):
            world.addObject(Actor(), 0, 0)

    ##
    # Test that the add object function captures invalid x and y coordinates
    # @throws ValueError when x and y are not within the boundaries of grid
    # expected = ValueError.class
    #
    def testAddObjectValueError(self):
        world = World(10, 10)

        with self.assertRaises(ValueError):
            world.addObject(Actor(), 1000, -1)

    ##
    # Test that the add object function captures null values
    # @throws RuntimeError when the value being added is null
    # expected = RuntimeError.class
    #
    def testAddObjectRuntimeError(self):
        world = World(1, 1)
        with self.assertRaises(RuntimeError):
            world.addObject(None, 0, 0)


if __name__ == '__main__':
    unittest.main()

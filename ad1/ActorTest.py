#!/usr/bin/env python
# coding: UTF-8
#
## @package ActorTest

from Actor import Actor
import unittest


##
#
# ActorTest class
#
# Resolução da AD1 2020.2 - Prog. de Interfaces Gráficas - TSC/UFF
# @author ARIADNE GONÇALVES PINHEIRO
# Matrícula: 19113050151
# Pólo: Duque de Caxias
# @date 26/08/2020
#

class ActorTest(unittest.TestCase):
    ##
    # Test the initialization of actor
    #
    def testConstructorAndGetMethods(self):
        actor = Actor()

        self.assertEqual(0, actor.getX())
        self.assertEqual(0, actor.getY())
        self.assertEqual(None, actor.getWorld())

    ##
    # Test the exception that happens when the world is null upon setting a location
    # @throws RuntimeError when the world is null
    # expected = RuntimeError.class
    #
    def testSetLocationRuntimeError(self):
        actor = Actor()
        with self.assertRaises(RuntimeError):
            actor.setLocation(2, 1)


if __name__ == '__main__':
    unittest.main( )

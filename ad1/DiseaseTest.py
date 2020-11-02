#!/usr/bin/env python
# coding: UTF-8
#
## @package DiseaseTest

from Disease import Disease
from MyWorld import MyWorld
import unittest


##
#
# DiseaseTest class
#
# Resolução da AD1 2020.2 - Prog. de Interfaces Gráficas - TSC/UFF
# @author ARIADNE GONÇALVES PINHEIRO
# Matrícula: 19113050151
# Pólo: Duque de Caxias
# @date 26/08/2020
#

class DiseaseTest(unittest.TestCase):
    ##
    # Test the initial value of strength in different quadrants
    #
    def testStrength(self):
        myworld = MyWorld()
        disease = Disease()
        self.assertEqual(1, disease.getStrength())

        diseases = myworld.initDiseases("1")

        # Quadrant 1
        myworld.initLocations("200,200", diseases)
        myworld.initGrowthConditions("10.0,15.0,2.0", diseases)
        myworld.initTemps("12;13;14;15")

        diseases[0].act()

        self.assertEqual(True, diseases[0].getStrength() > 1)


if __name__ == '__main__':
    unittest.main()

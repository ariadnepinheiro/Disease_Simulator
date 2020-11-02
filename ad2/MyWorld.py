#!/usr/bin/env python
# coding: UTF-8
#
# @package MyWorld
# @author Ariadne Pinheiro
# @date 08/10/2020
#
# This MyWorld class is a sub-class of the World class.
#
##

from World import World
from IWorld import IWorld
from Disease import Disease
import sys


class MyWorld(World, IWorld):
    ##
    # Call the constructor of the World class with the
    # width and height of 8 and 8 pixels, with 64 cells , respectively .
    #
    # Initialize a list to keep the average temperature
    # of each world region ( quadrant ).
    #
    # Call the prepare () method .
    #
    def __init__(self):
        super().__init__(8, 8)
        #  Initialize an array to keep the average temperature of each world region (quadrant).
        self.avgTemp = [None, None, None, None]
        #  Start the iteration as 0
        self.__iterations = 0
        #  Call the prepare() method.
        self.prepare()

    ##
    # This method overrides the act () method in the World class .
    # This method prints :
    #
    # " Iteration < ITRID >: World disease strength is < WorldDisease >"
    # where < ITRID > is replaced by the current iteration number and
    # < WorldDisease > is replaced by the returned value of
    # getSumStrength () in 2 decimal places .
    # An example is below .
    #
    # Iteration 0: World disease strength is 2.00
    # Iteration 1: World disease strength is 3.00
    #
    def act(self):
        print("Iteration {}: World disease strength is {:.2f}".format(self.__iterations, self.getSumStrength()))
        self.__iterations += 1

    ##
    # Prepare the world . Open a text file named
    # " simulation . config " in the current path
    # ( directly under the project directory ).
    # Parse the configuration file for the number
    # of Disease objects , the cell locations of these objects ,
    # the growth rates , and the temperature ranges associated
    # with individual growth rates .
    # Read Section 4 on the content of the configuration file
    # before reading the rest .
    # @throws IOError when there are problems with opening a file, reading, or writing to a file.
    #
    def prepare(self):
        try:
            inputFile = 'simulation.config'
            with open(inputFile, 'r') as arq:
                lines = arq.read().splitlines()
                for line in lines:
                    line = line.split('=')
                    func, params = line[0], line[1]
                    if func.lower() == 'NumDiseases'.lower():
                        diseases = self.initDiseases(params)
                    elif func.lower() == 'Locations'.lower():
                        if diseases is None:
                            raise IOError
                        self.initLocations(params, diseases)
                    elif func.lower() == 'DiseasesGrowth'.lower():
                        self.initGrowthConditions(params, diseases)
                    elif func.lower() == 'Temperature'.lower():
                        self.initTemps(params)
        except IOError:
            print("Terminating the program.")
            sys.exit(-1)

    ##
    # Set the temperature of the region of the world
    # to the value of temp .
    # The quadID indicates the region .
    # The valid value is between [0 , 3].
    # Any value of float is accepted for temp .
    # @throws ValueError if the quad id is not within 0 and 3
    #
    def setTemp(self, quad, temp):
        if not 0 <= quad <= 3:
            raise ValueError
        self.avgTemp[quad] = temp

    ##
    # Return the temperature of the world region with
    # the ID of quadID .
    # The valid value is between zero and three inclusive .
    # @throws ValueError if the quad id is not within 0 and 3
    #
    def getTemp(self, quad):
        if not 0 <= quad <= 3:
            raise ValueError
        return self.avgTemp[quad]

    ##
    # Create Disease objects ; the number of the objects equals
    # to the value passed in numDisStr .
    # Return a list of object references to the created
    # Disease objects .
    #
    # An example of a valid numDisStr is below .
    #
    # Ex : "2"
    #
    # If numDisStr is None or it cannot be converted to
    # a positive integer , print a message on screen
    # " Check the NumDiseases line in simulation . config ."
    # and return None .
    #
    # No exceptions are thrown .
    #
    def initDiseases(self, numDisStr):
        try:
            numDisStr = int(numDisStr)
            diseases = []
            for i in range(numDisStr):
                diseases.append(Disease())
            return diseases
        except:
            print("Check the NumDiseases line in simulation.config.")
            return None

    ##
    # Add each Disease object into the MyWorld object
    # implementing this method according to the information
    # in locationStr .
    #
    # An example of a locationStr is "200 ,200;400 ,480".
    # This means that the first Disease is planted at cell
    # (200 ,200) and the second Disease is at cell (400 , 480).
    #
    # If the locationStr is empty or not in the correct format
    # or does not have all the cell coordinates of all the
    # Disease objects , print on screen
    # " Check the Locations line in simulation . config "
    # and return -1.
    #
    # Return 0 for a successful initialization
    # of the Disease locations . No exceptions are thrown .
    #
    def initLocations(self, locationsStr, diseaseArr):
        try:
            coords = locationsStr.split(";")
            i = 0
            x, y = [], []
            for coord in coords:
                location = coord.split(",")
                x.append(int(location[0]))
                y.append(int(location[1]))
            while True:
                self.addObject(diseaseArr[i], x[i], y[i])
                i += 1
                if i >= len(x):
                    break
        except:
            print("Check the Locations line in simulation.config")
            return -1
        return 0

    ##
    # Set the lower bound and upper bound temperature
    # and the growth rate for each disease according
    # to the input growthStr .
    # An example of a valid string for two Disease objects is :
    #
    # Ex : "10.0 ,15.0 ,2.0;10.0 ,13.0 ,3.0"
    #
    # If growthStr is empty or not in the correct format
    # or does not have all the growth for all the Disease objects
    # in the Disease array , print on screen
    # " Check the DiseasesGrowth line in simulation . config ."
    # and return -1.
    #
    # Return 0 for a successful
    # initialization of the Disease growth conditions .
    # No exceptions are thrown .
    #
    def initGrowthConditions(self, growthStr, diseaseArr):
        try:
            growth = growthStr.split(";")
            for key, value in enumerate(growth):
                rates = value.split(',')
                diseaseArr[key].setGrowthCondition(float(rates[0]), float(rates[1]), float(rates[2]))
        except:
            print("Check the DiseasesGrowth line in simulation.config.")
            return -1
        return 0

    ## Set the temperature for each quadrant of the MyWorld
    # according to the value of the tempStr .
    # An example of tempStr is below .
    # The region temperatures for regions 0 , 1 , 2 , and 3
    # are 12 , 20 , 50 , and 100 , respectively .
    #
    # Return 0 for a successful initialization of
    # the quadrant temperatures . No exceptions are thrown .
    #
    # Ex : "12;20;50;100"
    #
    # If tempStr is empty or not in the correct format
    # or does not have all the temperatures of all
    # the regions , print on screen
    # " Check the Temperature line in simulation . config ."
    # and return -1
    #
    def initTemps(self, tempStr):
        try:
            temps = tempStr.split(";")
            for quad, temp in enumerate(temps):
                self.setTemp(int(quad), float(temp))
        except:
            print("Check the temperatures line in simulation.config")
            return -1
        return 0

    ## Return the total disease strength of all the diseases
    # in the class implementing this interface .
    #
    def getSumStrength(self):
        diseases = self.getObjects()
        totalStrength = 0
        for disease in diseases:
            totalStrength += disease.getStrength()
        return totalStrength

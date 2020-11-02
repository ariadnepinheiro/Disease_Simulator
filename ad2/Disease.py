#!/usr/bin/env python
# coding: UTF-8
#
# @package Disease
# @author Ariadne Pinheiro
# @date 26/08/2020
#
# This Disease class is a sub-class of the Actor class.
##

from Actor import Actor
from IDisease import IDisease


class Disease(Actor, IDisease):
    ##
    # Constructor.
    # - Call its superclass’s default constructor.
    # - Initialize the lower bound and the upper bound temperatures for the
    #   growth rate to 0.
    # - Set the growth rate to 0.
    # - Set the disease strength to 1.
    #
    def __init__(self):
        super(Disease, self).__init__()
        ### Rate at which the disease grows when subjected to the appropriate temperature range.    
        self.__growthRate = 0.0
        ### Minimum temperature for the disease development.
        self.__lowerTemp = 0.0
        ### Maximum temperature for the disease development.
        self.__higherTemp = 0.0
        ### Disease strength.
        self.__dStrength = 1.0
        ### Quadrant position
        self.__quadrant = 0

    ##
    # Sets the disease growth rate, lower temperature and higher temperature.
    #
    # @param lTemp Lower bound temperature for the disease to grow at this gRate.
    # @param hTemp Upper bound temperature for the disease to grow at this gRate.
    # @param gRate The growth rate.
    #
    def setGrowthCondition(self, lTemp, hTemp, gRate):
        self.__growthRate = gRate
        self.__lowerTemp = lTemp
        self.__higherTemp = hTemp

    ##
    # Returns the disease growth rate, lower temperature and higher temperature.
    #
    # @return growth rate, lower temp and higher temp
    #
    def getGrowthCondition(self):
        return self.__growthRate, self.__lowerTemp, self.__higherTemp

    ## Returns the quadrant of this disease.
    #
    # @return 0, 1, 2 or 3.
    #
    def getQuadrant(self):
        if 0 <= self.getX() < self.getWorld().getWidth() / 2 and 0 <= self.getY() < self.getWorld().getHeight() / 2:
            self.__quadrant = 0
        elif self.getWorld().getWidth() / 2 <= self.getX() < self.getWorld().getWidth() and 0 <= self.getY() < self.getWorld().getHeight() / 2:
            self.__quadrant = 1
        elif 0 <= self.getX() < self.getWorld().getWidth() / 2 and self.getWorld().getHeight() / 2 <= self.getY() < self.getWorld().getHeight():
            self.__quadrant = 2
        else:
            self.__quadrant = 3

        return self.__quadrant

    ##
    # Print on screen in the format "Iteration <ID>: Actor <Actor ID>."
    # The @f$<ID>@f$ is replaced by the current iteration number.
    # @f$<Actor ID>@f$ is replaced by the unique ID of the Actor object that performs
    # the act() method.
    #
    def act(self):
        temperature = self.getWorld().getTemp(self.getQuadrant())
        if self.__lowerTemp <= temperature <= self.__higherTemp:
            self.__dStrength *= self.__growthRate

    ##
    # Return the disease strength of this object.
    #
    # @return disease strength of the object.
    #
    def getStrength(self):
        return self.__dStrength

    ##
    # Return a string with the strength, growth and quadrant of this disease.
    #
    def __str__(self):
        st = super(Disease, self).__str__()
        st += 'strength = %f\n' % self.getStrength()
        st += 'growth = %f, %f, %f\n' % self.getGrowthCondition()
        st += 'quadrant = %d, temp = %d\n' % (self.getQuadrant(), self.getWorld().getTemp(self.getQuadrant()))
        return st

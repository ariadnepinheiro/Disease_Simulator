#!/usr/bin/env python
# coding: UTF-8
#
# @package IWorld
# @author Ariadne Pinheiro
# @date 26/08/2020
#
# Interface IWorld allows initializing and setting diseases for a world.
##

try:  # python >= 3.4
    from abc import ABC, ABCMeta, abstractmethod
except ImportError:  # python 2
    from abc import ABCMeta, abstractmethod

    ABC = object


class IWorld(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def prepare(self): pass

    @abstractmethod
    def setTemp(self, quad, temp): pass

    @abstractmethod
    def getTemp(self, quad): pass

    @abstractmethod
    def getObjects(self): pass

    @abstractmethod
    def getSumStrength(self): pass

    @abstractmethod
    def initDiseases(self, numDisStr): pass

    @abstractmethod
    def initLocations(self, locationsStr, diseaseArr): pass

    @abstractmethod
    def initGrowthConditions(self, growthStr, diseaseArr): pass

    @abstractmethod
    def initTemps(self, tempStr): pass

#!/usr/bin/env python
# coding: UTF-8
#
## @package IDisease
#  
#  Disease Interface.
#

try:  # python >= 3.4
    from abc import ABC, ABCMeta, abstractmethod
except ImportError:  # python 2
    from abc import ABCMeta, abstractmethod

    ABC = object


##
# Interface IDisease allows setting the strength and growth condition of a disease.
#
# Resolução da AD1 2020.2 - Prog. de Interfaces Gráficas - TSC/UFF
# @author ARIADNE GONÇALVES PINHEIRO
# Matrícula: 19113050151
# Pólo: Duque de Caxias
# @date 26/08/2020
#

class IDisease(ABC):
    __metaclass__ = ABCMeta

    ## 
    # Set the growth condition of a Disease object to gRate. The value of
    # gRate gets multiplied to the current disease strength only when the
    # disease is located in the world region with the average temperature in
    # between the values of lTemp and hTemp.
    #
    @abstractmethod
    def setGrowthCondition(self, lTemp, hTemp, gRate):
        pass

    ### Return the disease strength of the object implements this interface.
    @abstractmethod
    def getStrength(self):
        pass
